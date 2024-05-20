import socket as sk
import time
from concurrent.futures import ThreadPoolExecutor
from module.util.logger_conf import logger

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024


def hello_from_server(cliSock: sk.socket) -> None:
    data: bytes = cliSock.recv(BUFFER_SIZE)
    logger.info(f"from client: {data.decode('utf-8')}")
    pass


def listen() -> None:
    logger.info(f"server is listening...")
    with sk.socket(family=sk.AF_INET, type=sk.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        with ThreadPoolExecutor(max_workers=5) as clientExecutor:
            cliSock, addr = sock.accept()
            fut = clientExecutor.submit(hello_from_server, cliSock)
            fut.result()
            pass
        pass
    logger.info(f"server shutdown!")
    return 1
    pass


def create_socket() -> None:
    logger.info(f"server thread is starting ...")
    with ThreadPoolExecutor(max_workers=1) as serverExecutor:
        # for _ in serverExecutor.map(listen, []): pass
        fut = serverExecutor.submit(listen)
        fut.result()
        pass
    logger.info(f"server thread is listening ...")
    pass


if __name__ == "__main__":
    create_socket()
    time.sleep(10.0)
    pass
