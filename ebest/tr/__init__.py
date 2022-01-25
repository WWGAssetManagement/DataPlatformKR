from ebest.tr.login import Login
from ebest.tr.stocklist import StockList
from ebest.tr.sectorcode import SectorCode
from ebest.tr.themacode import ThemaCode
from ebest.tr.sectorstock import SectorStock
from ebest.tr.management_insincerity_investment_precautions import ManagementInsincerityInvestmentPrecautions

def get_login():
    return Login()

def get_stock_list(gubun):
    """
    :param gubun:  구분 0: 전체, 1: 코스피, 2: 코스닥
    :return:
    """
    return StockList(gubun=gubun)

def get_sector_code():
    return SectorCode()

def get_thema_code():
    return ThemaCode()

def get_sector_stock(upcode):
    """
    :param upcode: 업종코드
    :return:
    """
    return SectorStock(upcode=upcode)

def get_management_insincerity_investment_precautions(jongchk):
    """
    :param jongchk: 종목체크
    :return:
    """
    return ManagementInsincerityInvestmentPrecautions(jongchk=jongchk)