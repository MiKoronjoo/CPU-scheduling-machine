import threading
import time

import matplotlib.pyplot as plt


class Process(object):
    """
    :param p_id:
    :type p_id: string
    :param burst_time:
    :type burst_time: integer
    :param arrival_time:
    :type arrival_time: integer
    """

    def __init__(self, p_id: str, burst_time: int, arrival_time: int) -> None:
        self.id = p_id
        self.burst_time = burst_time
        self.p_time = ProcessTime(arrival_time)
        self.start = False
        self.first_burst_time = burst_time

    def __bool__(self) -> bool:
        return bool(self.burst_time)

    def __str__(self) -> str:
        return str(self.id)

    def __lt__(self, other: 'Process') -> bool:
        return self.burst_time < other.burst_time

    def run_ms(self) -> None:
        time.sleep(1 / SPEED)
        self.burst_time -= 1


class ProcessTime(object):
    """
    :param arrival_time:
    :type arrival_time: integer
    """
    def __init__(self, arrival_time: int) -> None:
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.start_time = 0
        self.end_time = 0

    @property
    def response_time(self) -> int:
        return self.start_time - self.arrival_time

    @property
    def turnaround_time(self) -> int:
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

    def __init__(self) -> None:
        self._burst_times = {}
        self._burst_times2 = {}
        self._io_times = {}
        self._arrival_times = {}
        self._timer = 0
        self._ready_queue = []
        self._io_works = []
        self._last_arrive = 0
        self._gantt_chart = []
        self.real_tat = 0
        self.idle = 0

    def clear(self) -> None:
        """
        Clears OS object data
        """
        self._burst_times.clear()
        self._burst_times2.clear()
        self._io_times.clear()
        self._arrival_times.clear()
        self._timer = 0
        self._ready_queue.clear()
        self._io_works.clear()
        self._last_arrive = 0
        self._gantt_chart.clear()
        self.real_tat = 0
        self.idle = 0

    @property
    def process_count(self) -> int:
        return len(self._burst_times)

    @property
    def cpu_util(self) -> float:
        if self._timer:
            return (self._timer - self.idle) / self._timer
        return 1.0

    @property
    def throughput(self) -> float:
        if self._timer:
            return len(self._ready_queue) * 1000 / self._timer
        return 1.0

    @property
    def avg_tt(self) -> float:
        if self._ready_queue:
            return sum([prs.p_time.turnaround_time for prs in self._ready_queue]) / len(self._ready_queue)
        return 0.0

    @property
    def avg_rt(self) -> float:
        if self._ready_queue:
            return sum([prs.p_time.response_time for prs in self._ready_queue]) / len(self._ready_queue)
        return 0.0

    @property
    def avg_wt(self) -> float:
        if self._ready_queue:
            return sum([prs.p_time.waiting_time for prs in self._ready_queue]) / len(self._ready_queue)
        return 0.0

    def __str__(self) -> str:
        return f'Avg Turnaround Time: {self.avg_tt}\n' \
            f'Avg Response Time:   {self.avg_rt}\n' \
            f'Avg Waiting Time:    {self.avg_wt}\n' \
            f'Throughput:          {self.throughput}\n' \
            f'CPU Utilization:     {self.cpu_util}\n'

    def set_data(self, file_path: str) -> None:
        """
        Sets OS object data with file that read from file_path
        :param file_path:
        :type file_path: string
        """
        prs_data = csv_parser(file_path)
        self.clear()
        for p_id, arrival_time, burst_time1, io_time, burst_time2 in prs_data:
            self._burst_times[p_id] = int(burst_time1)
            self._burst_times2[p_id] = int(burst_time2)
            self._io_times[p_id] = int(io_time)
            self._arrival_times[p_id] = int(arrival_time)
        self._last_arrive = max(self._arrival_times.values())
        self.reset_timer()

    def process_generator(self, p_id: str, burst_time: int) -> None:
        """
        Generates a process with args
        :param p_id:
        :type p_id: string
        :param burst_time:
        :type burst_time: integer
        """
        for prs in self._ready_queue:
            if prs.id == p_id:
                # prs.burst_time = burst_time
                break
        else:
            self._ready_queue.append(Process(p_id, burst_time, self._arrival_times[p_id]))

    def reset_timer(self) -> None:
        self._timer = 0

    @property
    def timer(self) -> int:
        return self._timer

    def add_to_chart(self, prs: Process = None) -> None:
        """
        Adds process id to gantt chart
        :param prs:
        :type prs: Process
        """
        if prs is None:
            self._gantt_chart.append('')
        else:
            self._gantt_chart.append(prs.id)

    def show_gantt(self, title: str = '') -> None:
        """
        Shows the gantt chart
        :param title: optional:
        :type title: string
        """
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

    def new_to_ready(self) -> None:
        """
        Moves arrival processes to ready queue
        """
        for prs in self._io_works:
            if self._arrival_times[prs.id] == self._timer:
                self._ready_queue.append(prs)
                self._io_works.remove(prs)
        for p_id in self._arrival_times:
            if self._arrival_times[p_id] == self._timer:
                self.process_generator(p_id, self._burst_times[p_id])

    def cpu_to_io(self, prs: Process) -> None:
        """
        Moves the process to I/O
        :param prs:
        :type prs: Process
        """
        at2 = self._io_times[prs.id] + self._timer
        self._io_times[prs.id] = 0
        self._arrival_times[prs.id] = at2
        prs.burst_time = self._burst_times2[prs.id]
        self._io_works.append(prs)
        self._ready_queue.remove(prs)
        self._last_arrive = max(self._last_arrive, self._arrival_times[prs.id])

    def wait(self) -> None:
        """
        Waits for one time unit (CPU is idle)
        """
        time.sleep(1 / SPEED)
        self._timer += 1
        self.add_to_chart()
        self.idle += 1

    def fcfs(self) -> None:
        """
        Runs FCFS algorithm with OS object data
        """
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
                            prs.p_time.waiting_time = prs.p_time.turnaround_time - prs.first_burst_time
                    break
            else:
                self.wait()
        self.real_tat = time.time() - start_time

    def spn(self) -> None:  # sjf
        """
        Runs SPN algorithm with OS object data
        """
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

    def rr(self) -> None:
        """
        Runs RR algorithm with OS object data
        """
        start_time = time.time()
        while any(self._ready_queue) or self._timer <= self._last_arrive:
            self.new_to_ready()
            nothing = True
            for prs in self._ready_queue:
                counter = 0
                for _ in range(TIME_Q):
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
                            break
                        else:
                            prs.p_time.end_time = self._timer
                            break
            if nothing:
                self.wait()
        self.real_tat = time.time() - start_time

    def srt(self) -> None:
        """
        Runs SRT algorithm with OS object data
        """
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
    """
    :param data_path: Optional:
    :type data_path: string
    """
    def __init__(self, data_path: str = '') -> None:
        self.os = OS()
        self._data_path = data_path

    def set_data_path(self, data_path: str) -> None:
        """
        Sets data_path
        :param data_path:
        :type data_path: string
        """
        self._data_path = data_path

    def sim_exe(self) -> str:  # simultaneous execution
        """
        Runs FCFS, SPN, RR and SRT algorithms simultaneous
        :return: Execution results
        :rtype: string
        """
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
        return f'* FCFS\n{t1}\n' \
            f'* SPN \n{t2}\n' \
            f'* RR  \n{t3}\n' \
            f'* SRT \n{t4}\n'


def csv_parser(file_path: str) -> list:
    """
    Pares the data that read from file
    :param file_path:
    :type file_path: string
    :rtype: list
    """
    with open(file_path, 'r') as file:
        lst = [[elm for elm in line.strip().split(',')][:5] for line in file.readlines()[1:]]
    return lst


SPEED = 1000
TIME_Q = 5
if __name__ == '__main__':
    machine = Machine('data.csv')
    machine.sim_exe()
