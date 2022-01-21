from ebest.tr.login import Login
from ebest.tr.stocklist import StockList
from ebest.tr.sectorcode import SectorCode
from ebest.tr.themacode import ThemaCode

def get_login():
    return Login()

def get_stock_list(gubun):
    return StockList(gubun=gubun)

def get_sector_code():
    return SectorCode()

def get_thema_code():
    return ThemaCode()