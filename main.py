import ebest
from dotenv import load_dotenv
import time

if __name__ == "__main__":
    load_dotenv()
    login = ebest.get_login()
    accounts = login.get_account()
    stock_list = ebest.get_stock_list(gubun=0)
    stock_list.to_sql()

    sector_code = ebest.get_sector_code()
    sector_dicts = sector_code.to_dicts()
    upcodes = list(map(lambda x: x['upcode'], sector_dicts))

    for upcode in upcodes:
        ebest.get_sector_stock(upcode=upcode).to_sql()
        time.sleep(10)

    thema_code = ebest.get_thema_code()
    thema_code.to_sql()