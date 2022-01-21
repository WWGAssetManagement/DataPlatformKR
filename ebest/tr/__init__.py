from ebest.tr.login import Login
from ebest.tr.stocklist import StockList


def get_login():
    return Login()


def get_stock_list(gubun):
    return StockList(gubun=gubun)

