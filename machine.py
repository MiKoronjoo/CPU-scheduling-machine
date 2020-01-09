import pprint
import threading
import time

import matplotlib.pyplot as plt


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


class OS(object):
    colors = [
        '#dd0000',  # red
        '#009900',  # green
        '#002db3',  # blue
        '#fce300',  # yellow
        '#ff7300',  # orange
        '#990099',  # purple
        '#00e6e6',  # cyan
        '#ff99ff',  # pink
        '#421100',  # brown pod
        '#ddc15f',  # tacha
        '#320042',  # blackcurrant
        '#87b100',  # citrus
        '#423200',  # mikado
        '#00b187',  # persian green
        '#004232',  # british racing green
    ]

    def __init__(self):
        self._burst_times = {}
        self._burst_times2 = {}
        self._io_times = {}
        self._arrival_times = {}
        self._timer = 0
        self._ready_queue = []
        self._last_arrive = 0
        self._gantt_chart = []
        self.real_tat = 0
        self.idle = 0

    @property
    def process_count(self):
        return len(self._burst_times)

    @property
    def cpu_util(self):
        if self._timer:
            return (self._timer - self.idle) / self._timer
        return 1.0

    @property
    def throughput(self):
        if self._timer:
            return len(self._ready_queue) * 1000 / self._timer
        return 1.0

    @property
    def avg_tt(self):
        if self._ready_queue:
            return sum([prs.p_time.turnaround_time for prs in self._ready_queue]) / len(self._ready_queue)
        return 0.0

    @property
    def avg_rt(self):
        if self._ready_queue:
            return sum([prs.p_time.response_time for prs in self._ready_queue]) / len(self._ready_queue)
        return 0.0

    @property
    def avg_wt(self):
        if self._ready_queue:
            return sum([prs.p_time.waiting_time for prs in self._ready_queue]) / len(self._ready_queue)
        return 0.0

    def set_data(self, file_path):
        prs_data = csv_parser(file_path)
        self._arrival_times.clear()
        self._burst_times.clear()
        self._io_times.clear()
        self._burst_times2.clear()
        self._gantt_chart.clear()
        self._ready_queue.clear()
        for p_id, arrival_time, burst_time1, io_time, burst_time2 in prs_data:
            self._burst_times[p_id] = int(burst_time1)
            self._burst_times2[p_id] = int(burst_time2)
            self._io_times[p_id] = int(io_time)
            self._arrival_times[p_id] = int(arrival_time)
        self._last_arrive = max(self._arrival_times.values())
        self.reset_timer()

    def process_generator(self, p_id, burst_time):
        for prs in self._ready_queue:
            if prs.id == p_id:
                prs.burst_time = burst_time
                break
        else:
            self._ready_queue.append(Process(p_id, burst_time, self._arrival_times[p_id]))

    def reset_timer(self):
        self._timer = 0

    @property
    def timer(self):
        return self._timer

    def add_to_chart(self, prs: Process = None):
        if prs is None:
            self._gantt_chart.append('')
        else:
            self._gantt_chart.append(prs.id)

    def show_gantt(self, title=''):
        color_dict = {}
        i = 0
        for x in self._burst_times:
            if x and x not in color_dict:
                color_dict[x] = OS.colors[i]
                i += 1
        fig, gnt = plt.subplots()
        gnt.set_ylim(0, 10)
        gnt.set_xlabel('millisecond since start')
        gnt.set_ylabel('CPU')
        gnt.set_title(title)
        gnt.set_yticks([])
        s = 0
        for x in self._gantt_chart:
            if x:
                gnt.broken_barh([(s, 1)], (0, 2), facecolors=color_dict[x])
            s += 1
        print('****', title, '****')
        for x in color_dict:
            rgb = tuple(int(color_dict[x][i + 1:i + 2], 16) * 16 for i in (0, 2, 4))
            print('\033[38;2;%d;%d;%dm███\033[0m P_ID:' % rgb, x)
        plt.show()

    def new_to_ready(self):
        for p_id in self._arrival_times:
            if self._arrival_times[p_id] == self._timer:
                self.process_generator(p_id, self._burst_times[p_id])

    def cpu_to_io(self, prs):
        at2 = self._io_times[prs.id] + self._timer
        self._io_times[prs.id] = 0
        self._arrival_times[prs.id] = at2
        prs.burst_time = self._burst_times2[prs.id]
        self._last_arrive = max(self._last_arrive, self._arrival_times[prs.id])

    def wait(self):
        time.sleep(1 / SPEED)
        self._timer += 1
        self.add_to_chart()
        self.idle += 1

    def fcfs(self):
        start_time = time.time()
        while any(self._ready_queue) or self._timer <= self._last_arrive:
            self.new_to_ready()
            for prs in self._ready_queue:
                if prs:
                    while prs:
                        if not prs.start:
                            prs.start = True
                            prs.p_time.start_time = self._timer
                        prs.run_ms()
                        self._timer += 1
                        self.add_to_chart(prs)
                        self.new_to_ready()
                    else:
                        if self._io_times[prs.id]:
                            self.cpu_to_io(prs)
                        else:
                            prs.p_time.end_time = self._timer
                            prs.p_time.waiting_time = prs.p_time.response_time  # for FCFS
                    break
            else:
                self.wait()
        self.real_tat = time.time() - start_time

    def spn(self):  # sjf
        start_time = time.time()
        while any(self._ready_queue) or self._timer <= self._last_arrive:
            self.new_to_ready()
            temp_rq = [prs for prs in self._ready_queue if prs]  # remove executed processes (have no burst time)
            if temp_rq:
                min_prs = min(temp_rq)  # choose shortest process
                while min_prs:
                    if not min_prs.start:
                        min_prs.start = True
                        min_prs.p_time.start_time = self._timer
                    min_prs.run_ms()
                    self._timer += 1
                    self.add_to_chart(min_prs)
                    self.new_to_ready()
                else:
                    if self._io_times[min_prs.id]:
                        self.cpu_to_io(min_prs)
                    else:
                        min_prs.p_time.end_time = self._timer
                        min_prs.p_time.waiting_time = min_prs.p_time.response_time  # for SPN
            else:
                self.wait()
        self.real_tat = time.time() - start_time

    def rr(self):
        start_time = time.time()
        while any(self._ready_queue) or self._timer <= self._last_arrive:
            self.new_to_ready()
            nothing = True
            for prs in self._ready_queue:
                counter = 0
                for _ in range(5):
                    if prs:
                        nothing = False
                        if not prs.start:
                            prs.start = True
                            prs.p_time.start_time = self._timer
                        prs.run_ms()
                        self._timer += 1
                        self.add_to_chart(prs)
                        counter += 1
                        for other in self._ready_queue:
                            if other and other is not prs:
                                other.p_time.waiting_time += 1
                        self.new_to_ready()
                    if counter and not prs:
                        if self._io_times[prs.id]:
                            self.cpu_to_io(prs)
                        else:
                            prs.p_time.end_time = self._timer
            if nothing:
                self.wait()
        self.real_tat = time.time() - start_time

    def srt(self):
        start_time = time.time()
        while any(self._ready_queue) or self._timer <= self._last_arrive:
            self.new_to_ready()
            temp_rq = [prs for prs in self._ready_queue if prs]
            if temp_rq:
                min_prs = min(temp_rq)  # choose shortest remaining time
                if not min_prs.start:
                    min_prs.start = True
                    min_prs.p_time.start_time = self._timer
                min_prs.run_ms()
                self._timer += 1
                self.add_to_chart(min_prs)
                for other in self._ready_queue:
                    if other and other is not min_prs:
                        other.p_time.waiting_time += 1
                if not min_prs:
                    if self._io_times[min_prs.id]:
                        self.cpu_to_io(min_prs)
                    else:
                        min_prs.p_time.end_time = self._timer
            else:
                self.wait()
        self.real_tat = time.time() - start_time


class Machine(object):
    def __init__(self, data_path=''):
        self.os = OS()
        self._data_path = data_path

    def set_data_path(self, data_path):
        self._data_path = data_path

    def sim_exe(self):  # simultaneous execution
        if not self._data_path:
            raise ValueError('data_path is not set')
        t1 = OS()
        t2 = OS()
        t3 = OS()
        t4 = OS()
        t1.set_data(self._data_path)
        t2.set_data(self._data_path)
        t3.set_data(self._data_path)
        t4.set_data(self._data_path)
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
        print(f'spn \t{t2.timer} ^_^ {t2.real_tat * SPEED}')
        print(f'rr  \t{t3.timer} ^_^ {t3.real_tat * SPEED}')
        print(f'srt \t{t4.timer} ^_^ {t4.real_tat * SPEED}')
        t1.show_gantt('First In First Out')
        t2.show_gantt('Shortest Process Next')
        t3.show_gantt('Round-Robin')
        t4.show_gantt('Shortest Remaining Time')


def csv_parser(file_path):
    with open(file_path, 'r') as file:
        lst = [[elm for elm in line.strip().split(',')][:5] for line in file.readlines()[1:]]
    return lst


SPEED = 1000
if __name__ == '__main__':
    machine = Machine('data.csv')
    machine.sim_exe()
