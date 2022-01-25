import os
from sqlalchemy import create_engine, Table
from daeshin.models.models import MinutePriceModel
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
from config.settings import META
from multiprocessing import Pool

def rename_columns(x: str):
    if "_price" in x:
        return x.replace("_price", "")
    else:
        return x

def insert_minute_price(path):
    print(path)
    LOCAL_DAESHIN_DATABASE = os.environ.get("LOCAL_DAESHIN_DATABASE")
    engine = create_engine(LOCAL_DAESHIN_DATABASE)
    conn = engine.connect()
    minute_table = Table(MinutePriceModel.__tablename__, META, autoload_with=engine)
    price = pd.read_pickle(path)
    price.rename(columns=rename_columns, inplace=True)
    price_dict = price.to_dict('records')
    conn.execute(minute_table.insert().prefix_with("IGNORE"), price_dict)
    del conn


if __name__ == "__main__":
    load_dotenv()
    file_paths = Path('../data').glob("*.pkl")

    pool = Pool(processes=16)
    pool.map(insert_minute_price, list(file_paths))
    pool.close()
    pool.join()