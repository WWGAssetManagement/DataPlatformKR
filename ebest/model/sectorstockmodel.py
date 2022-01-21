from sqlalchemy import Column, VARCHAR, Float, DATETIME, PrimaryKeyConstraint
from config.settings import BASE

class SectorStockModel(BASE):
    __tablename__ = "tb_sector_stock"
    date = Column(DATETIME)
    upcode = Column(VARCHAR(5))
    hname = Column(VARCHAR(20))
    price = Column(Float)
    sign = Column(VARCHAR(1))
    change = Column(Float)
    diff = Column(Float)
    volume = Column(Float)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    sojinrate = Column(Float)
    beta = Column(Float)
    perx = Column(Float)
    frgsvolume = Column(Float)
    orgsvolume = Column(Float)
    diff_vol = Column(Float)
    shcode = Column(VARCHAR(6))
    total = Column(Float)
    value = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(shcode, date, upcode),
        {},
    )


