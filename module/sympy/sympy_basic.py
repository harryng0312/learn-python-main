import sympy as sp
import sympy.plotting as spplot
import matplotlib.figure as fig
import matplotlib.pyplot as plt
import numpy as np

from module.util.logger_conf import logger


def find_limit() -> None:
    x: sp.Symbol = sp.symbols("x");
    logger.info(f"x = {x}")
    lim = sp.limit(sp.sin(x), x, 0, dir="-")
    logger.info(f"lim:{lim}")
    return


def find_derivate() -> None:
    return

def find_integrate() -> None:
    x = sp.symbols('x')
    expr = x**2 + x + 1 
    integrate = sp.integrate(expr, x)
    # sp.init_session()
    logger.info(f"integrate:{integrate}")
    logger.info(f"integrate eval:{integrate.subs({x:3})}")
    sp.plot(integrate)
    # spplot.plot3d(integrate)
    return

def plot_trigonometric_func() -> None:
    x = sp.symbols("x")
    sin_func = sp.sin(x)
    cos_func = sp.cos(x+sp.pi)
    tan_func = sp.tan(x)
    x_1_func = 2/x
    graph_sin_cos: sp.plotting.plot.Plot = sp.plot(sin_func, cos_func, show=False)
    graph_tan: sp.plotting.plot.Plot = sp.plot(tan_func, show=False, ylim=(-10, 10))
    graph_1_x: sp.plotting.plot.Plot = sp.plot(x_1_func, show=False, ylim=(-10, 10))
    # graph_tan.show()
    graph_1_x.show()
    # fig, axs = plt.subplots(nrows=1, ncols=1)
    # fig.subplots_adjust(left=0.25, bottom=0.25)
    # t = np.arange(start=-10, stop=10, step = 0.001)
    # ax1 = fig.add_subplot(1, 1, 1)
    # ax2 = fig.add_subplot(2, 1, 2)
    # ax1.plot(t)
    # plt.show()

    return

if __name__ == "__main__":
    # sp.init_printing()
    # find_integrate()
    plot_trigonometric_func()
    pass