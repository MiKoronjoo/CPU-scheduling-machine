import threading
import time


class Machine(object):
    pass


class OS(object):
    def __init__(self):
        self.burst_times = {}
        self.arrival_times = {}
        self.timer = 0
        self.ready_queue = []
        self.real_tat = 0
        self.last_arrive = 0
        self.idle = 0

    def set_data(self, file_path):
        prs_data = csv_parser(file_path)
        self.burst_times.clear()
        self.arrival_times.clear()
        for p_id, arrival_time, burst_time in prs_data:
            self.burst_times[p_id] = int(burst_time)
            self.arrival_times[p_id] = int(arrival_time)
        self.last_arrive = max(self.arrival_times.values())

    def process_generator(self, p_id, burst_time):
        self.ready_queue.append(Process(p_id, burst_time, self.arrival_times[p_id]))

    def reset_timer(self):
        self.timer = 0

    def new_to_ready(self):
        for p_id in self.arrival_times:
            if self.arrival_times[p_id] == self.timer:
                self.process_generator(p_id, self.burst_times[p_id])

    def wait(self):
        time.sleep(1 / SPEED)
        self.timer += 1
        self.idle += 1

    def fcfs(self):
        start_time = time.time()
        while any(self.ready_queue) or self.timer <= self.last_arrive:
            self.new_to_ready()
            for prs in self.ready_queue:
                if prs:
                    while prs:
                        if not prs.start:
                            prs.start = True
                            prs.p_time.start_time = self.timer
                        prs.run_ms()
                        self.timer += 1
                        self.new_to_ready()
                    prs.p_time.end_time = self.timer
                    prs.p_time.waiting_time = prs.p_time.response_time  # for FCFS
                    break
            else:
                self.wait()
        self.real_tat = time.time() - start_time

    def spn(self):  # sjf
        start_time = time.time()
        while any(self.ready_queue) or self.timer <= self.last_arrive:
            self.new_to_ready()
            temp_rq = [prs for prs in self.ready_queue if prs]  # remove executed processes (have no burst time)
            if temp_rq:
                min_prs = min(temp_rq)  # choose shortest process
                while min_prs:
                    if not min_prs.start:
                        min_prs.start = True
                        min_prs.p_time.start_time = self.timer
                    min_prs.run_ms()
                    self.timer += 1
                    self.new_to_ready()
                min_prs.p_time.end_time = self.timer
                min_prs.p_time.waiting_time = min_prs.p_time.response_time  # for SPN
            else:
                self.wait()
        self.real_tat = time.time() - start_time

    def rr(self):
        start_time = time.time()
        while any(self.ready_queue) or self.timer <= self.last_arrive:
            self.new_to_ready()
            nothing = True
            for prs in self.ready_queue:
                counter = 0
                for _ in range(5):
                    if prs:
                        nothing = False
                        if not prs.start:
                            prs.start = True
                            prs.p_time.start_time = self.timer
                        prs.run_ms()
                        self.timer += 1
                        counter += 1
                        for other in self.ready_queue:
                            if other and other is not prs:
                                other.p_time.waiting_time += 1
                        self.new_to_ready()
                    if counter and not prs:
                        prs.p_time.end_time = self.timer
            if nothing:
                self.wait()
        self.real_tat = time.time() - start_time

    def srt(self):
        start_time = time.time()
        while any(self.ready_queue) or self.timer <= self.last_arrive:
            self.new_to_ready()
            temp_rq = [prs for prs in self.ready_queue if prs]
            if temp_rq:
                min_prs = min(temp_rq)  # choose shortest remaining time
                if not min_prs.start:
                    min_prs.start = True
                    min_prs.p_time.start_time = self.timer
                min_prs.run_ms()
                self.timer += 1
                for other in self.ready_queue:
                    if other and other is not min_prs:
                        other.p_time.waiting_time += 1
                if not min_prs:
                    min_prs.p_time.end_time = self.timer
            else:
                self.wait()
        self.real_tat = time.time() - start_time


class Process(object):
    def __init__(self, p_id, burst_time, arrival_time):
        self.id = p_id
        self.burst_time = burst_time
        self.p_time = ProcessTime(arrival_time)
        self.start = False

    def __bool__(self):
        return bool(self.burst_time)

    def __str__(self):
        return str(self.id)

    def __lt__(self, other):
        return self.burst_time < other.burst_time

    def run_ms(self):
        time.sleep(1 / SPEED)
        self.burst_time -= 1


class ProcessTime(object):
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.start_time = 0
        self.end_time = 0

    @property
    def response_time(self):
        return self.start_time - self.arrival_time

    @property
    def turnaround_time(self):
        return self.end_time - self.arrival_time


def csv_parser(file_path):
    with open(file_path, 'r') as file:
        lst = [[elm for elm in line.strip().split(',')][:3] for line in file.readlines()[1:]]
    return lst


def sim_exe(data_path):  # simultaneous execution
    t1 = OS()
    t2 = OS()
    t3 = OS()
    t4 = OS()
    t1.set_data(data_path)
    t2.set_data(data_path)
    t3.set_data(data_path)
    t4.set_data(data_path)
    th1 = threading.Thread(name='fcfs', target=t1.fcfs)
    th2 = threading.Thread(name='spn', target=t2.spn)
    th3 = threading.Thread(name='rr', target=t3.rr)
    th4 = threading.Thread(name='srt', target=t4.srt)
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th1.join()
    th2.join()
    th3.join()
    th4.join()
    print(f'fcfs\t{t1.timer} ^_^ {t1.real_tat * SPEED}')
    print(f'spn\t\t{t2.timer} ^_^ {t2.real_tat * SPEED}')
    print(f'rr\t\t{t3.timer} ^_^ {t3.real_tat * SPEED}')
    print(f'srt\t\t{t4.timer} ^_^ {t4.real_tat * SPEED}')


if __name__ == '__main__':
    SPEED = 10
    sim_exe('data.csv')
