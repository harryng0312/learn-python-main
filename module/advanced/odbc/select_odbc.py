import os
import pyodbc

from module.advanced.odbc.conn_odbc import create_conn, close_conn
from module.util.logger_conf import logger


def select_one() -> None:
    sql: str = "SELECT customer_id, cust_name, city, grade, salesman_id " \
                + "FROM customer WHERE customer_id = ?"
    with create_conn() as conn:
        cursor: pyodbc.Cursor = conn.cursor()
        # cursor.execute(sql, 1)
        cursor.execute(sql, 3001)
        colums: list[str] = [x[0] for x in cursor.description]
        row: pyodbc.Row = cursor.fetchone()
        if row:
            row_dict: dict = dict(zip(colums, row))
            # logger.info(f"id: {row.customer_id} name: {row[1]}")
            logger.info(f"id: {row_dict['customer_id']} name: {row_dict['cust_name']}")
            pass
        pass
    pass


def select_all() -> None:
    sql: str = "SELECT customer_id, cust_name, city, grade, salesman_id " \
                + "FROM customer WHERE city = ?"
    with create_conn() as conn:
        cursor: pyodbc.Cursor = conn.cursor()
        cursor.execute(sql, "New York")
        # cursor: pyodbc.Cursor = conn.execute(sql, "New York")
        colums: list[str] = [x[0] for x in cursor.description]
        rows: pyodbc.Row = cursor.fetchall()
        # row_dict: dict = dict(zip(colums, row))
        for row in rows:
            row_dict: dict = dict(zip(colums, row))
            # logger.info(f"id: {row.customer_id} name: {row[1]}")
            logger.info(f"id: {row_dict['customer_id']} name: {row_dict['cust_name']}")
            pass
        pass
    # close_conn(conn)
    pass


if __name__ == "__main__":
    select_one()
    # select_all()

    logger.info("pwd:{0}".format(os.getenv("PYTHONPATH")))
    # print("pwd:{0}".format(os.getenv("PYTHONPATH")))
    pass