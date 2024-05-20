import asyncio
import asyncio.events as evt
import contextlib as ctx
import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future, wait
from module.util.logger_conf import logger

TOTAL: int = 0

async def eternity(param: list[str]):
    # Sleep for one hour
    logger.info(f"into thread function{param} at {datetime.datetime.now()}")
    await asyncio.sleep(delay=0.6)
    logger.info(f"out to thread function{param} at {datetime.datetime.now()}")
    print('yay!')

def async_thread_function_1(param: list[str]):
    # Wait for at most 1 second
    loop: evt.AbstractEventLoop = asyncio.new_event_loop() # for ThreadPool
    # loop: evt.AbstractEventLoop = asyncio.get_event_loop() # for ProcessPool
    try:
        loop.run_until_complete(eternity(param))
    except TimeoutError:
        print('timeout!')
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.run_until_complete(loop.shutdown_default_executor())
        loop.close()
        del loop
    return


def multi_thread() -> None:
    count: int = 3
    threads: list[Thread] = []
    global TOTAL
    with ThreadPoolExecutor(max_workers=4) as pool:
    # with ProcessPoolExecutor(max_workers=4) as pool:
        for _ in pool.map(async_thread_function_1, [1, 1, 1, 1], timeout=1.6): pass
        pass
    logger.info(f"resource:{TOTAL}")
    pass


if __name__ == "__main__":
    multi_thread()
    pass
