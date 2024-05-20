import pandas as pd
import numpy as np
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


def select_data_corr(frm_fact: pd.DataFrame, frm_dim: pd.DataFrame) -> None:
    logger.info(f"\n{frm_dim}")
    logger.info(f"corr\n{frm_dim.corr()}")
    
    return


if __name__ == "__main__":
    # show_dataframe()
    # show_dataseries()
    frm_fact = load_csv(FACT_DATA_FILE)
    frm_dim = load_csv(DIM_DATA_FILE)
    # select_data(frm_fact)
    select_data_corr(frm_fact=frm_fact, frm_dim=frm_dim)
    pass
