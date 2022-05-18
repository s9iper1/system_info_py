import os
import multiprocessing
import re
import subprocess

import psutil
import platform


def print_system_memory():
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
    mem_gib = mem_bytes / (1024. ** 3)
    print(f'total ram available in GB {int(round(mem_gib, 2))}')


def print_system_cores():
    count = multiprocessing.cpu_count()
    print(f'cpu counts using multiprocessing : {count}')
    print(f'thread: {psutil.cpu_count(logical=True)}')
    print(f'cores: {psutil.cpu_count(logical=False)}')


def print_system_os_info():
    system = platform.system()
    kernel = platform.release()
    machine = platform.machine()
    print(f'system :{system} kernel: {kernel} machine:{machine}')


if __name__ == '__main__':
    print_system_memory()
    print_system_cores()
    print_system_os_info()
