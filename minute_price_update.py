import time

from tqdm import tqdm
import daeshin
from config.settings import EBEST_SESSION
import config
from ebest.model.models import StockListModel
import pandas as pd

if __name__ == "__main__":
    log = config.get_log()
    session = EBEST_SESSION()
    tickers = list(map(lambda x: x[0], session.query(StockListModel.shcode).all()))
    dates = pd.date_range(start="2021-09-01", end="2022-01-24")

    minute_price = daeshin.get_minute_price()
    for ticker in tqdm(tickers):
        for date in dates:
            try:
                time.sleep(.3)
                print(f"종목코드: {ticker}: 날짜: {date}")
                start = (date - pd.Timedelta(days=1)).strftime("%Y%m%d")
                end = date.strftime("%Y%m%d")
                minute_price.set(ticker, int(start), int(end)).to_sql()
            except Exception as e:
                log.logger.debug(f"{ticker} Error: {e}")