import logging
import sys

from module import ROOT_DIR


# LOG_FILE = "../../../data/log/app.log"
LOG_FILE = ROOT_DIR + "/../data/log/app.log"

# logging.basicConfig(filename=LOG_FILE,
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG)

logger = logging.getLogger("log")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler(filename=LOG_FILE, encoding='utf8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


# logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

