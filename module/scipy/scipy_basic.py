import numpy as np
import numpy.lib as npl
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

from module.util.logger_conf import logger
from scipy import special



if __name__ == "__main__":
    nd_grid_1: tuple = np.mgrid[0:5, 0:4]
    logger.info(f"\n{nd_grid_1}")
    a: complex = complex(real=0, imag=1)
    logger.info(f"\n{a**2}")
    pass