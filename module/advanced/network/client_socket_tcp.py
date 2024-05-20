import socket
from datetime import datetime
from module.util.logger_conf import logger

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024


def create_socket() -> None:
    logger.info(f"client is connecting...")
    greeting = f"hi server at:{ datetime.now() }"
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(greeting, "utf-8"))
        pass
    logger.info(f"client disconnected!")
    pass


if __name__ == "__main__":
    create_socket()
    pass
