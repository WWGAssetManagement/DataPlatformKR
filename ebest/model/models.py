from sqlalchemy import Column, VARCHAR, FLOAT, DATETIME, PrimaryKeyConstraint
from config.settings import BASE


class ManagementInsincerityInvestmentPrecautionsModel(BASE):
    __tablename__ = "tb_management_insincerity_investmentprecautions"
    hname = Column(VARCHAR(20))
    price = Column(FLOAT)
    sign = Column(VARCHAR(1))
    change = Column(FLOAT)
    diff = Column(FLOAT)
    volume = Column(FLOAT)
    date = Column(DATETIME)
    tprice = Column(FLOAT)
    tchange = Column(FLOAT)
    tdiff = Column(FLOAT)
    reason = Column(VARCHAR(4))
    shcode = Column(VARCHAR(6))
    edate = Column(VARCHAR(8))
    __table_args = (
        PrimaryKeyConstraint(shcode, date),
        {},
    )


class SectorCodeModel(BASE):
    __tablename__ = "tb_sector_code"
    upcode = Column(VARCHAR(5), primary_key=True, nullable=False)
    hname = Column(VARCHAR(30))


class SectorStockModel(BASE):
    __tablename__ = "tb_sector_stock"
    date = Column(DATETIME)
    upcode = Column(VARCHAR(5))
    hname = Column(VARCHAR(20))
    price = Column(FLOAT)
    sign = Column(VARCHAR(1))
    change = Column(FLOAT)
    diff = Column(FLOAT)
    volume = Column(FLOAT)
    open = Column(FLOAT)
    high = Column(FLOAT)
    low = Column(FLOAT)
    sojinrate = Column(FLOAT)
    beta = Column(FLOAT)
    perx = Column(FLOAT)
    frgsvolume = Column(FLOAT)
    orgsvolume = Column(FLOAT)
    diff_vol = Column(FLOAT)
    shcode = Column(VARCHAR(6))
    total = Column(FLOAT)
    value = Column(FLOAT)
    __table_args__ = (
        PrimaryKeyConstraint(shcode, date, upcode),
        {},
    )


class StockListModel(BASE):
    __tablename__ = "tb_stock_list"
    date = Column(DATETIME)
    hname = Column(VARCHAR(30))
    shcode = Column(VARCHAR(8))
    expcode = Column(VARCHAR(20))
    etfgubun = Column(VARCHAR(3))
    uplmtprice = Column(FLOAT)
    dnlmtprice = Column(FLOAT)
    jnilclose = Column(FLOAT)
    memedan = Column(VARCHAR(7))
    recprice = Column(FLOAT)
    gubun = Column(VARCHAR(1))

    __table_args = (
        PrimaryKeyConstraint(shcode, date),
        {},
    )


class ThemaCodeModel(BASE):
    __tablename__ = "tb_thema_code"
    tmcode = Column(VARCHAR(5), primary_key=True, nullable=False)
    tmname = Column(VARCHAR(20))


class InvestWarningSupensionTradeLiquidatedTradeModel(BASE):
    __tablename__ = "tb_investwarning_supensiontrade_liquidatedtrade"
    hname = Column(VARCHAR(20))
    price = Column(FLOAT)
    sign = Column(VARCHAR(1))
    change = Column(FLOAT)
    diff = Column(FLOAT)
    volume = Column(FLOAT)
    date = Column(DATETIME)
    edate = Column(DATETIME)
    shcode = Column(VARCHAR(6))
    __table_args = (
        PrimaryKeyConstraint(shcode, date),
        {},
    )
