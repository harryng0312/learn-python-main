from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future, wait
# from collections.abc import Mapping
import datetime
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../')))
from module.util.logger_conf import logger


TOTAL: int = 0

def thread_function(param: list[str]) -> None:
    logger.info(f"into thread function{param} at {datetime.datetime.now()}")
    time.sleep(2.0)
    logger.info(f"out to thread function{param} at {datetime.datetime.now()}")
    pass

def thread_function_2(param1: int, param2: int) -> None:
    global TOTAL
    TOTAL += param1 * param2
    time.sleep(0.5)
    pass

def single_thread() -> None:
    x: Thread = Thread(target = thread_function, args=(["test 1", "test 2"],))
    logger.info(f"Start:\t\t{datetime.datetime.now()}")
    x.start()
    logger.info(f"Finish:\t{datetime.datetime.now()}")
    x.join()
    pass

def multi_thread() -> None:
    count: int = 3
    threads: list[Thread] = []
    global TOTAL
    for i in range(0, count):
        tmp: Thread = Thread(target = thread_function_2, args=(1,2))
        threads.append(tmp)
        pass
    # thread_function_2(1)
    # logger.info(f"TOTAL:{TOTAL}")
    for t in threads:
        t.start()
        pass
    for t in threads:
        t.join()
        pass
    logger.info(f"resource:{TOTAL}")
    pass

if __name__ == "__main__":
    nowStr: str = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    # single_thread()
    multi_thread()

# print(f"__name__:{__name__}")