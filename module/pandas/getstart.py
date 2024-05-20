import pandas as pd
import numpy as np
from pandas import DataFrame
from module.util.logger_conf import logger


def show_dataframe() -> None:
    logger.info("show dataframe")
    # default_dataset = pd.DataFrame(data={"cars": "", "passings": 0}, columns=["cars", "passings"])
    # default_dataset = pd.Series(data=["", 0])
    mydataset: map = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
    }
    myvar: pd.DataFrame = pd.DataFrame(data=mydataset, columns=["cars", "passings"])
    myvarFilter: pd.Series = myvar["passings"] > 2
    myvarFilter2:pd.Series = myvar["passings"] < 7
    logger.info(f"ori\n{myvar}")
    logger.info(f"where\n{myvar.where(cond=myvarFilter & myvarFilter2, other='')}")
    logger.info(f"query\n{myvar.query(expr='passings > 2')}")
    logger.info(f"[...]\n{myvar[myvar['passings'] < 7]}")
    return


def show_dataseries() -> None:
    logger.info("show dataserie")
    a = [1, 7, 2]
    myvar = pd.Series(data=a, index = ["x", "y", "z"])
    logger.info(f"\n{myvar}\n|{myvar['y']}|")
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(data=calories, index = ["day1", "day2"])   
    logger.info(f"\n{myvar.where(cond=myvar > 400)}\n|{myvar['day2']}|")
    return


if __name__ == "__main__":
    show_dataframe()
    # show_dataseries()
    pass
