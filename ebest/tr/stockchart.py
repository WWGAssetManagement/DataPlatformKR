"""
주식 차트 조회
"""
import time
from ebest.core.xa_query_events import XAQueryEvents
from ebest.core.ebest_database import EbestDataBase
from ebest.model.models import StockChartModel


class StockChart(XAQueryEvents, EbestDataBase):
    tr_code = 't4201'
    results = None
    shcode = None
    start_date = None
    end_date = None
    gubun = None

    def __init__(self, shcode, start_date, end_date, gubun="2"):
        """

        :param shcode: 005930
        :param start_date: 20100101
        :param end_date: 20200101
        :param gubun: 0: tick, 1: 분, 2: 일, 3: 월
        """
        XAQueryEvents.__init__(self, tr_code=self.tr_code)
        EbestDataBase.__init__(self, model=StockChartModel)
        self.shcode = shcode
        self.start_date = start_date
        self.end_date = end_date
        self.gubun = gubun
        self.__request()
        self.__get_rows()

    def __request(self):
        self._set_field_data(self.inblock, "shcode", 0, self.shcode)
        self._set_field_data(self.inblock, "gubun", 0, self.gubun)
        self._set_field_data(self.inblock, "qrycnt", 0, "500")
        self._set_field_data(self.inblock, "tdgb", 0, "0")
        self._set_field_data(self.inblock, "sdate", 0, self.start_date)
        self._set_field_data(self.inblock, "edate", 0, self.end_date)
        self._request(0)
        self._receive()

    def __get_rows(self):
        index_num = self._get_block_count(self.outblock1)
        self.results = list(map(lambda x: self.__get_row(x), range(index_num)))
        print()

    def __get_row(self, index) -> dict:
        date = self._get_field_data(self.outblock1, "date", index).strip()
        time = self._get_field_data(self.outblock1, "time", index).strip()
        open = self._get_field_data(self.outblock1, "open", index).strip()
        high = self._get_field_data(self.outblock1, "high", index).strip()
        low = self._get_field_data(self.outblock1, "low", index).strip()
        close = self._get_field_data(self.outblock1, "close", index).strip()
        jdiff_vol = self._get_field_data(self.outblock1, "jdiff_vol", index).strip()
        value = self._get_field_data(self.outblock1, "value", index).strip()
        jongchk = self._get_field_data(self.outblock1, "jongchk", index).strip()
        rate = self._get_field_data(self.outblock1, "rate", index).strip()
        pricechk = self._get_field_data(self.outblock1, "pricechk", index).strip()
        ratevalue = self._get_field_data(self.outblock1, "ratevalue", index).strip()

        return {
            'shcode': self.shcode,
            'date': date,
            'time': time,
            'open': open,
            'high': high,
            'low': low,
            'close': close,
            'jdiff_vol': jdiff_vol,
            'value': value,
            'jongchk': jongchk,
            'rate': rate,
            'pricechk': pricechk,
            'ratevalue': ratevalue
        }

    def to_dicts(self):
        return self.results

    def to_sql(self):
        self._save(self.results)
