from ebest.tr.login import Login
from ebest.tr.stocklist import StockList
from ebest.tr.sectorcode import SectorCode
from ebest.tr.themacode import ThemaCode
from ebest.tr.sectorstock import SectorStock
from ebest.tr.management_insincerity_investment_precautions import ManagementInsincerityInvestmentPrecautions
from ebest.tr.investwarning_supensiontrade_liquidatedtrade import InvestWarningSupensionTradeLiquidatedTrade
from ebest.tr.stockchart import StockChart


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


def get_investwarning_supensiontrade_liquidatedtrade(jongchk):
    """
    :param jongchk: 종목체크 0 or 1
    :return:
    """
    return InvestWarningSupensionTradeLiquidatedTrade(jongchk)


def get_stock_chart(shcode, start_date, end_date, gubun="2"):
    """
    :param shcode: 005930
    :param start_date: 20100101
    :param end_date: 20200101
    :param gubun: 0: tick, 1: 분, 2: 일, 3: 월
    """
    return StockChart(shcode, start_date, end_date, gubun=gubun)
