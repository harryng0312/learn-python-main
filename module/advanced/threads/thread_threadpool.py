from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future, wait
from multiprocessing import Manager, Process
# from collections.abc import Mapping
import datetime
import time
import os
import sys
import numpy as np

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../')))
from module.util.logger_conf import logger


TOTAL: int = 0


def thread_function(param: list[str]) -> None:
    logger.info(f"into thread function{param} at {datetime.datetime.now()} - PID:{os.getpid()}")
    time.sleep(2)
    logger.info(f"out to thread function{param} at {datetime.datetime.now()}")
    pass


def thread_function_2(param1: int, param2: int, lock: Manager) -> None:
    global TOTAL
    logger.info(f"into thread function{param1} at {datetime.datetime.now()} - PID:{os.getpid()}")
    with lock:
        TOTAL += param1 * param2
    time.sleep(2)
    pass


def single_thread() -> None:
    x: Thread = Thread(target=thread_function, args=(["test 1", "test 2"],))
    logger.info(f"Start:\t\t{datetime.datetime.now()}")
    x.start()
    logger.info(f"Finish:\t{datetime.datetime.now()}")
    x.join()
    pass


def multi_thread() -> None:
    count: int = 3
    threads: list[Thread] = []
    global TOTAL
    with ThreadPoolExecutor(max_workers=count) as pool, Manager() as manager:
        # with ProcessPoolExecutor(max_workers=3) as pool:
        size = 100
        param = np.random.randint(low=1, high=10, size=(size,))
        for _ in pool.map(thread_function_2, param, param, manager, timeout=600): 
            pass
        pass
    logger.info(f"resource:{TOTAL}")
    return


def multi_thread_2() -> None:
    count: int = 100
    threads: list[Thread] = []
    global TOTAL
    TOTAL = 0
    size = 100
    param = np.random.randint(low=1, high=10, size=(size,))
    with Manager() as manager:
        for i in range(0, count):
            x: Thread = Thread(target=thread_function_2, args=(param[i], param[i], manager))
            threads.append(x)
            # logger.info(f"Start:\t\t{datetime.datetime.now()}")
            x.start()
            # logger.info(f"Finish:\t{datetime.datetime.now()}")
            # x.join()
            pass
        for t in threads:
            t.join()
            pass
    logger.info(f"resource:{TOTAL}")
    return

def multi_process() -> None:
    size = 10
    global TOTAL
    TOTAL = 0
    with Manager() as manager:
        with ProcessPoolExecutor(max_workers=size) as pool:
            # with ProcessPoolExecutor(max_workers=3) as pool:
            size = 100
            param = np.random.randint(low=1, high=10, size=(size,))
            # logger.info({param**2})
            lock = [manager.Lock() for i in range(0, size)]
            for t in pool.map(thread_function_2, param, param, lock, timeout=600):
                pass
            pass
    logger.info(f"resource:{TOTAL}")
    return

def multi_process_2() -> None:
    count = 10
    size = 100
    global TOTAL
    TOTAL = 0
    processes = []
    with Manager() as manager:
        for i in range(1, count):
            # with ProcessPoolExecutor(max_workers=3) as pool:
            size = 100
            param = np.random.randint(low=1, high=10, size=(size,))
            lock = manager.Lock()
            param = manager.Value(param)
            # logger.info({param**2})
            p = Process(target=thread_function_2, args=(param[i], param[i], lock))
            processes.append(p)
            p.start()
            pass
        for process in processes:
            process.join()
            pass
    logger.info(f"resource:{TOTAL}")
    return

if __name__ == "__main__":
    nowStr: str = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    # single_thread()
    # multi_thread()
    multi_thread_2()
    multi_process()
    pass

# print(f"__name__:{__name__}")
