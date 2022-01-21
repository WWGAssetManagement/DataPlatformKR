from sqlalchemy import Column, DATETIME, Float, VARCHAR, PrimaryKeyConstraint
from config.settings import BASE


class StockListModel(BASE):
    __tablename__ = "tb_stock_list"
    date = Column(DATETIME)
    hname = Column(VARCHAR(30))
    shcode = Column(VARCHAR(8))
    expcode = Column(VARCHAR(20))
    etfgubun = Column(VARCHAR(3))
    uplmtprice = Column(Float)
    dnlmtprice = Column(Float)
    jnilclose = Column(Float)
    memedan = Column(VARCHAR(7))
    recprice = Column(Float)
    gubun = Column(VARCHAR(1))

    __table_args = (
        PrimaryKeyConstraint(shcode, date),
        {},
    )
