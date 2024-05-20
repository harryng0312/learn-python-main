import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from module.util.logger_conf import logger
from module.conf import PROJECT_DIR
from datetime import datetime as dt


DIM_DATA_FILE = "".join([PROJECT_DIR, "/data/csv/DIM_customers.csv"])
FACT_DATA_FILE = "".join([PROJECT_DIR, "/data/csv/FACT_InternetSales.csv"])


def load_csv(file_name: str) -> pd.DataFrame:
    frm_data = pd.read_csv(filepath_or_buffer=file_name)
    return frm_data


def select_data(data_frm: pd.DataFrame) -> None:
    data_frm['OrderDateKey'] = pd.to_datetime(arg=data_frm['OrderDateKey'], format=r"%Y%m%d")
    data_frm['DueDateKey'] = pd.to_datetime(arg=data_frm['DueDateKey'], format=r"%Y%m%d")
    data_frm['ShipDateKey'] = pd.to_datetime(arg=data_frm['ShipDateKey'], format=r"%Y%m%d")
    date_comp: dt = dt.strptime("2022/06/01", r"%Y/%m/%d")
    data_frm.query("ProductKey > 600 & OrderDateKey >= @date_comp", inplace=True)
    data_frm.sort_values(by=["ProductKey", "OrderDateKey"], ascending=[True, False], inplace=True)
    logger.info(f"\n{data_frm}")
    # filter_result: pd.DataFrame = data_frm[(data_frm['ProductKey'] > 600) & (data_frm['OrderDateKey'] > dt.strptime("2022/06/01", r"%Y/%m/%d"))]
    # filter_result.sort_values("ProductKey", ascending=True, inplace=True)
    # logger.info(f"{type(filter_result)}")
    # logger.info(f"\n{filter_result}")
    return


def select_data_join(frm_fact: pd.DataFrame, frm_dim: pd.DataFrame) -> pd.DataFrame:
    # frm_joined: pd.DataFrame = frm_fact.join(other=frm_dim, on=["CustomerKey"], how="inner", rsuffix="_r", lsuffix="_l")
    logger.info(f"{dt.now()}")
    frm_joined: pd.DataFrame = pd.merge(left=frm_dim, right=frm_fact, how="inner", left_on="CustomerKey", right_on="CustomerKey")
    # logger.info(f"{dt.now()}")
    # frm_joined.index += 1
    logger.info(f"{dt.now()}")
    logger.info(f"\n{frm_joined}")
    # logger.info(f"\n{frm_joined.take(indices=[1, 3])}")
    logger.info(f"{dt.now()}")
    
    return frm_joined


def plot(frm: pd.DataFrame) -> None:
    frm = frm.iloc[:100]
    logger.info(f"\n{frm}")
    frm_sum = frm.groupby(by=["CustomerKey"])["SalesOrderNumber"] \
        .count().to_frame().reset_index() \
        .rename(columns={"SalesOrderNumber":"sumOfSalesOrder"})
    frm_sum.sort_values(by=["CustomerKey"], ascending=[True], inplace=True)
    logger.info(f"\n{frm_sum}")
    frm_sum.plot.bar(x="CustomerKey", y="sumOfSalesOrder")
    # frm_sum.plot(kind="bar")
    # plt.bar(x=frm_sum["CustomerKey"], data=frm_sum["sumOfSalesOrder"])
    plt.show()    
    return

if __name__ == "__main__":
    # show_dataframe()
    # show_dataseries()
    frm_fact = load_csv(FACT_DATA_FILE)
    frm_dim = load_csv(DIM_DATA_FILE)
    # select_data(frm_fact)
    frm_join = select_data_join(frm_fact=frm_fact, frm_dim=frm_dim)
    plot(frm=frm_join)
    pass
