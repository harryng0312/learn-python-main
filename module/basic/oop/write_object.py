import pickle
import os
from Person import *
from module.util.logger_conf import logger

PERSON_FILE_PATH = "data/person/student.dat"

def write_to_bin_file(x: Student):
    with open(file=PERSON_FILE_PATH, buffering=1024, mode="+bw") as destFile:
        xData: bytes = pickle.dumps(obj=x)
        destFile.write(xData)
        destFile.flush
    pass


def read_from_bin_file():
    with open(file=PERSON_FILE_PATH, buffering=1024, mode="+br") as destFile:
        # endPos: int = os.path.getsize(PERSON_FILE_PATH)
        destFile.seek(0, os.SEEK_END)
        endPos: int = destFile.tell()
        destFile.seek(0, 0)
        xData: bytes = destFile.read(endPos)
        x:Student = pickle.loads(xData)
        # x: Student = pickle.load(destFile)
        logger.info(f"Student:{x}")
    pass


if __name__ == "__main__":
    x: Student = Student("Mike", "Olsen", 2019)
    write_to_bin_file(x)
    read_from_bin_file()
    pass
