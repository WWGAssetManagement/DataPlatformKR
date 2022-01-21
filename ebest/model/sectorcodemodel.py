from sqlalchemy import Column, VARCHAR
from config.settings import BASE


class SectorCodeModel(BASE):
    __tablename__ = "tb_sector_code"
    upcode = Column(VARCHAR(5), primary_key=True, nullable=False)
    hname = Column(VARCHAR(30))
