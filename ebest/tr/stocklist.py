"""
StockList: 주식종목조회
"""
from ebest.core.xa_query_events import XAQueryEvents
from ebest.core.ebest_database import EbestDataBase
from ebest.model.models import StockListModel
from datetime import datetime


class StockList(XAQueryEvents, EbestDataBase):
    tr_code = "t8430"
    results = None

    def __init__(self, gubun):
        """
        :param gubun: 구분 0: 전체, 1: 코스피, 2: 코스닥
        :return:
        """
        XAQueryEvents.__init__(self, tr_code=self.tr_code)
        EbestDataBase.__init__(self, model=StockListModel)
        self._set_field_data(self.inblock, "gubun", 0, gubun)
        self._request(0)
        self._receive()
        self.__get_rows()

    def to_dicts(self) -> list:
        return self.results

    def to_sql(self):
        self._save(self.results)

    def __get_rows(self):
        index_num = self._get_block_count(self.outblock)
        self.results = list(map(lambda x: self.__get_row(x), range(index_num)))

    def __get_row(self, index) -> dict:
        date = datetime.now().strftime("%Y-%m-%d")
        hname = self._get_field_data(self.outblock, 'hname', index).strip()
        shcode = self._get_field_data(self.outblock, 'shcode', index).strip()
        expcode = self._get_field_data(self.outblock, "expcode", index).strip()
        etfgubun = int(self._get_field_data(self.outblock, "etfgubun", index).strip())
        uplmtprice = int(self._get_field_data(self.outblock, "uplmtprice", index).strip())
        dnlmtprice = int(self._get_field_data(self.outblock, "dnlmtprice", index).strip())
        jnilclose = int(self._get_field_data(self.outblock, "jnilclose", index).strip())
        memedan = int(self._get_field_data(self.outblock, "memedan", index).strip())
        recprice = int(self._get_field_data(self.outblock, "recprice", index).strip())
        gubun = int(self._get_field_data(self.outblock, "gubun", index).strip())

        return {
            'date': date,
            'hname': hname,
            'shcode': shcode,
            'expcode': expcode,
            'etfgubun': etfgubun,
            'uplmtprice': uplmtprice,
            'dnlmtprice': dnlmtprice,
            'jnilclose': jnilclose,
            'memedan': memedan,
            'recprice': recprice,
            'gubun': gubun
        }
