from sqlalchemy import Column, VARCHAR
from config.settings import BASE


class ThemaCodeModel(BASE):
    __tablename__ = "tb_thema_code"
    tmcode = Column(VARCHAR(5), primary_key=True, nullable=False)
    tmname = Column(VARCHAR(20))
