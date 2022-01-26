"""
투자경고, 매매정지, 정리매매조회
"""
from ebest.core.xa_query_events import XAQueryEvents
from ebest.core.ebest_database import EbestDataBase
from ebest.model.models import InvestWarningSupensionTradeLiquidatedTradeModel
import time


class InvestWarningSupensionTradeLiquidatedTrade(XAQueryEvents, EbestDataBase):
    tr_code = "t1405"
    results = []

    def __init__(self, jongchk):
        XAQueryEvents.__init__(self, tr_code=self.tr_code)
        EbestDataBase.__init__(self, model=InvestWarningSupensionTradeLiquidatedTradeModel)
        self.jongchk = jongchk
        self.__request_first()
        self.__get_rows()

    def __request_first(self):
        self._set_field_data(self.inblock, "gubun", 0, "0")
        self._set_field_data(self.inblock, 'jongchk', 0, self.jongchk)
        self._request(0)
        self._receive()

    def __request_next(self, cts_shcode):
        self._set_field_data(self.inblock, 'cts_shcode', 0, cts_shcode)
        self._set_field_data(self.inblock, "gubun", 0, "0")
        self._set_field_data(self.inblock, 'jongchk', 0, self.jongchk)
        self._request(1)
        self._receive()

    def to_dicts(self):
        return self.results

    def to_sql(self):
        self._save(self.results)

    def __get_rows(self):
        index_num = self._get_block_count(self.outblock1)
        self.__get_row(index_num)

        while True:
            cts_shcode = self._get_field_data(self.outblock, 'cts_shcode', 0)
            if cts_shcode == "500003":
                break
            time.sleep(3)
            self.__request_next(cts_shcode)
            index_num = self._get_block_count(self.outblock1)
            self.__get_row(index_num)

    def __get_row(self, index_num):
        for index in range(index_num):
            hname = self._get_field_data(self.outblock1, "hname", index).strip()
            price = self._get_field_data(self.outblock1, "price", index).strip()
            sign = self._get_field_data(self.outblock1, "sign", index).strip()
            change = self._get_field_data(self.outblock1, "change", index).strip()
            diff = self._get_field_data(self.outblock1, "diff", index).strip()
            volume = self._get_field_data(self.outblock1, "volume", index).strip()
            date = self._get_field_data(self.outblock1, "date", index).strip()
            edate = self._get_field_data(self.outblock1, "edate", index).strip()
            shcode = self._get_field_data(self.outblock1, "shcode", index).strip()
            self.results.append({
                "hname": hname,
                "price": price,
                "sign": sign,
                "change": change,
                "diff": diff,
                "volume": volume,
                "date": date,
                "edate": edate,
                "shcode": shcode

            })
