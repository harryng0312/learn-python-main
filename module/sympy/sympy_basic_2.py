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

def solve_equation() -> None:
    x = sp.symbols("x")
    expr: sp.Eq = sp.Eq(x**6 + 2*x - 4, 0)
    nsolution = sp.nsolve(expr, 0)
    solution = sp.solve(f=expr, symbols=x)
    logger.info(f"type: {type(nsolution)} nsolution: {nsolution}")
    logger.info(f"type: {type(solution)} solution: {solution}")
    sp.CRootOf
    # sp.init_session()
    # sp.Integral(sp.sqrt(1/x), x)
    return

if __name__ == "__main__":
    # sp.init_printing()
    # find_integrate()
    solve_equation()
    pass