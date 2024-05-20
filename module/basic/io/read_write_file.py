from io import FileIO
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../')))
from module.util.logger_conf import logger

# from src.main.util.logger_conf import logger

FILE_NAME: str = "../../../data/matrix/mat1.txt"
FILE_NAME_2: str = "../../../data/matrix/mat1_copy.txt"


def copy_file(srcFilePath: str, destFilePath: str):
    srcFile: FileIO
    destFile: FileIO
    buffSize: int = 1_024
    buffer: bytes = None
    try:
        with open(file=srcFilePath, mode="+rb", buffering=buffSize) as srcFile, \
                open(file=destFilePath, mode="+bw", buffering=buffSize) as destFile:
            # with open(file = destFilePath, mode = "+bw", buffering = buffSize) as destFile:
            buffer = srcFile.read(buffSize)
            while (buffer):
                destFile.write(buffer)
                destFile.flush()
                buffer = srcFile.read(buffSize)
    except Exception as ex:
        logger.error(f"Exception: {ex}")
    finally:
        pass


if __name__ == "__main__":
    logger.info("copying...")
    copy_file(FILE_NAME, FILE_NAME_2)
    logger.info("copied!")
    pass
