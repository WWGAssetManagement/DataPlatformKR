from config.settings import BASE
from sqlalchemy import DATETIME, VARCHAR, Float, Column, PrimaryKeyConstraint


class MinutePriceModel(BASE):
    __tablename__ = "tb_minute_price"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(10))
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    transaction_amount = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(ticker, date),
        {},
    )
