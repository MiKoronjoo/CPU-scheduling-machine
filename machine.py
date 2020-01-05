import pprint
import threading
import copy
import time


class Machine(object):
    pass


class OS(object):
    def __init__(self):
        self.process_list = {}
        self.arr_times = {}
        self.timer = {
            'fcfs': 0,
            'spn': 0,
            'rr': 0,
            'srt': 0
        }
        self.tat = {}

    def process_generator(self, file_path):
        prs_data = csv_parser(file_path)
        temp = []
        for x in prs_data:
            temp.append(Process(x[0], int(x[2])))
            self.arr_times[x[0]] = int(x[1])
        algorithms = ['fcfs', 'spn', 'rr', 'srt']
        for alg in algorithms:
            self.process_list[alg] = copy.deepcopy(temp)

    def run(self):
        t1 = threading.Thread(name='fcfs', target=os.fcfs)
        t2 = threading.Thread(name='spn', target=os.spn)
        t3 = threading.Thread(name='rr', target=os.rr)
        t4 = threading.Thread(name='srt', target=os.srt)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        pprint.pprint(self.tat)

    def reset_timer(self):
        self.timer = {
            'fcfs': 0,
            'spn': 0,
            'rr': 0,
            'srt': 0
        }

    def delay(self, alg):
        time.sleep(1 / speed)
        self.timer[alg] += 1

    def fcfs(self):
        start_time = time.time()
        while any(self.process_list['fcfs']):
            for prs in self.process_list['fcfs']:
                if prs and self.arr_times[prs.id] <= self.timer['fcfs']:
                    self.timer['fcfs'] += prs.run()
                    break
            else:
                self.delay('fcfs')
        self.tat['fcfs'] = time.time() - start_time

    def spn(self):  # sjf
        start_time = time.time()
        while any(self.process_list['spn']):
            arr_prs = [prs for prs in self.process_list['spn'] if prs and self.arr_times[prs.id] <= self.timer['spn']]
            if arr_prs:
                min_prs = min(arr_prs)
                self.timer['spn'] += min_prs.run()
            else:
                self.delay('spn')
        self.tat['spn'] = time.time() - start_time

    def rr(self):
        start_time = time.time()
        while any(self.process_list['rr']):
            nothing = True
            for prs in self.process_list['rr']:
                for _ in range(5):
                    if prs and self.arr_times[prs.id] <= self.timer['rr']:
                        nothing = False
                        prs.run_ms()
                        self.timer['rr'] += 1
            if nothing:
                self.delay('rr')
        self.tat['rr'] = time.time() - start_time

    def srt(self):
        start_time = time.time()
        while any(self.process_list['srt']):
            arr_prs = [prs for prs in self.process_list['srt'] if prs and self.arr_times[prs.id] <= self.timer['srt']]
            if arr_prs:
                min_prs = min(arr_prs)
                min_prs.run_ms()
                self.timer['srt'] += 1
            else:
                self.delay('srt')
        self.tat['srt'] = time.time() - start_time


class Process(object):
    def __init__(self, p_id, burst_time):
        self.id = p_id
        self.burst_time = burst_time

    def __bool__(self):
        return bool(self.burst_time)

    def __str__(self):
        return str(self.id)

    def __lt__(self, other):
        return self.burst_time < other.burst_time

    def run_ms(self):
        time.sleep(1 / speed)
        self.burst_time -= 1

    def run(self):
        prev_bt = self.burst_time
        while self:
            self.run_ms()
        return prev_bt


def csv_parser(file_path):
    with open(file_path, 'r') as file:
        lst = [[elm for elm in line.strip().split(',')][:3] for line in file.readlines()[1:]]
    return lst


if __name__ == '__main__':
    speed = 10
    os = OS()
    os.process_generator('data.csv')
    print('START')
    os.run()
    print('END')
    os.reset_timer()
    os.process_generator('data2.csv')
    print('START')
    os.run()
    print('END')
