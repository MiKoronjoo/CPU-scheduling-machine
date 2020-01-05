import threading
import copy
import time


class Machine(object):
    pass


class OS(object):
    def __init__(self, prs_data):
        self.process_list = {}
        self.arr_times = {}
        self.now = 0

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

    def delay(self):
        time.sleep(1 / speed)
        self.now += 1

    def fcfs(self):
        start_time = time.time()
        while any(self.process_list['fcfs']):
            for prs in self.process_list['fcfs']:
                if prs and self.arr_times[prs.id] <= self.now:
                    self.now += prs.run()
                    break
            else:
                self.delay()
        print('fcfs:', time.time() - start_time)

    def spn(self):  # sjf
        start_time = time.time()
        while any(self.process_list['spn']):
            arr_prs = [prs for prs in self.process_list['spn'] if prs and self.arr_times[prs.id] <= self.now]
            if arr_prs:
                min_prs = min(arr_prs)
                self.now += min_prs.run()
            else:
                self.delay()
        print('spn:', time.time() - start_time)

    def rr(self):
        start_time = time.time()
        while any(self.process_list['rr']):
            nothing = True
            for prs in self.process_list['rr']:
                for _ in range(5):
                    if prs and self.arr_times[prs.id] <= self.now:
                        nothing = False
                        prs.run_ms()
                        self.now += 1
            if nothing:
                self.delay()
        print('rr:', time.time() - start_time)

    def srt(self):
        start_time = time.time()
        while any(self.process_list['srt']):
            arr_prs = [prs for prs in self.process_list['srt'] if prs and self.arr_times[prs.id] <= self.now]
            if arr_prs:
                min_prs = min(arr_prs)
                min_prs.run_ms()
                self.now += 1
            else:
                self.delay()
        print('srt:', time.time() - start_time)


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


def process_generator(file_path):
    pass


def csv_parser(file_path):
    with open(file_path, 'r') as file:
        lst = [[elm for elm in line.strip().split(',')][:3] for line in file.readlines()[1:]]
    return lst


if __name__ == '__main__':
    speed = 10
    data = csv_parser('data.csv')
    os = OS(data)
    print('START')
    os.run()
    print('END')
