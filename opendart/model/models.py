from sqlalchemy import Column, VARCHAR, FLOAT, DATETIME, PrimaryKeyConstraint
from config.settings import BASE


class CorpCodesModel(BASE):
    __tablename__ = "tb_corp_codes"
    corp_code = Column(VARCHAR(10))
    corp_name = Column(VARCHAR(30))
    stock_code = Column(VARCHAR(10))
    modify_date = Column(DATETIME)
    __table_args = (
        PrimaryKeyConstraint(corp_code, modify_date),
        {},
    )


class DartListDateExModel(BASE):
    __tablename__ = "tb_dart_list_date_ex"
    rcept_dt = Column(DATETIME)
    corp_cls = Column(VARCHAR(10))
    corp_code = Column(VARCHAR(10))
    corp_name = Column(VARCHAR(10))
    rcept_no = Column(VARCHAR(20))
    report_nm = Column(VARCHAR(40))
    flr_nm = Column(VARCHAR(40))
    rm = Column(VARCHAR(10))
    __table_args = (
        PrimaryKeyConstraint(rcept_dt, corp_code, report_nm),
        {},
    )


class DartListModel(BASE):
    __tablename__ = "tb_dart_list"
    corp_code = Column(VARCHAR(10))
    corp_name = Column(VARCHAR(20))
    stock_code = Column(VARCHAR(8))
    corp_cls = Column(VARCHAR(3))
    report_nm = Column(VARCHAR(40))
    rcept_no = Column(VARCHAR(20))
    fir_nm = Column(VARCHAR(20))
    rcept_dt = Column(DATETIME)
    rm = Column(VARCHAR(5))
    __table_args = (
        PrimaryKeyConstraint(stock_code, report_nm, rcept_dt),
        {},
    )
