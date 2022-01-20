import warnings
warnings.filterwarnings('ignore')
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
from multiprocessing import Pool




def save_data(table: str):
    DATABASE = os.environ.get("DataBase")
    print(table)
    engine = create_engine(DATABASE)
    conn = engine.connect()
    data_sql = f"SELECT * FROM {table}"
    price = pd.read_sql(data_sql, conn)
    ticker = table.split('_')[1]
    price['ticker'] = ticker
    price.to_pickle(f"data/{ticker}.pkl")
    del conn




if __name__ == "__main__":
    load_dotenv()
    DATABASE = os.environ.get("DataBase")
    engine = create_engine(DATABASE)
    conn = engine.connect()

    sql = "SHOW TABLES"
    tables = pd.read_sql(sql, conn)
    table_names = tables['Tables_in_cybos_plus_stock_minute_data']

    pool = Pool(processes=16)
    pool.map(save_data, table_names)
    pool.close()
    pool.join()