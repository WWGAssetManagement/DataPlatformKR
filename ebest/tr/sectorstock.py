"""
섹터별 종목 확인
"""
import time

from ebest.core.xa_query_events import XAQueryEvents
from ebest.core.ebest_database import EbestDataBase
from ebest.model.models import SectorStockModel
from datetime import datetime


class SectorStock(XAQueryEvents, EbestDataBase):
    tr_code = 't1516'
    date = None
    upcode = None
    results = []

    def __init__(self, upcode):
        XAQueryEvents.__init__(self, tr_code=self.tr_code)
        EbestDataBase.__init__(self, model=SectorStockModel)
        self.upcode = upcode
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.__request_first()
        self.__get_rows()

    def __request_first(self):
        self._set_field_data(self.inblock, 'upcode', 0, self.upcode)
        self._set_field_data(self.inblock, 'gubun', 0, ' ')
        self._set_field_data(self.inblock, 'shcode', 0, ' ')
        self._request(0)
        self._receive()

    def __request_next(self, shcode):
        self._set_field_data(self.inblock, 'upcode', 0, self.upcode)
        self._set_field_data(self.inblock, 'gubun', 0, '3')
        self._set_field_data(self.inblock, 'shcode', 0, shcode)
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
            shcode = self._get_field_data(self.outblock, 'shcode', 0)
            if shcode == "":
                break
            time.sleep(3)
            self.__request_next(shcode)
            index_num = self._get_block_count(self.outblock1)
            self.__get_row(index_num)

    def __get_row(self, index_num):
        for index in range(index_num):
            date = self.date
            upcode = self.upcode
            hname = self._get_field_data(self.outblock1, "hname", index).strip()
            price = self._get_field_data(self.outblock1, "price", index).strip()
            sign = self._get_field_data(self.outblock1, "sign", index).strip()
            change = self._get_field_data(self.outblock1, "change", index).strip()
            diff = self._get_field_data(self.outblock1, "diff", index).strip()
            volume = self._get_field_data(self.outblock1, "volume", index).strip()
            open = self._get_field_data(self.outblock1, "open", index).strip()
            high = self._get_field_data(self.outblock1, "high", index).strip()
            low = self._get_field_data(self.outblock1, "low", index).strip()
            sojinrate = self._get_field_data(self.outblock1, "sojinrate", index).strip()
            beta = self._get_field_data(self.outblock1, "beta", index).strip()
            perx = self._get_field_data(self.outblock1, "perx", index).strip()
            frgsvolume = self._get_field_data(self.outblock1, "frgsvolume", index).strip()
            orgsvolume = self._get_field_data(self.outblock1, "orgsvolume", index).strip()
            diff_vol = self._get_field_data(self.outblock1, "diff_vol", index).strip()
            shcode = self._get_field_data(self.outblock1, "shcode", index).strip()
            total = self._get_field_data(self.outblock1, "total", index).strip()
            value = self._get_field_data(self.outblock1, "value", index).strip()
            self.results.append({
                'date': date,
                'upcode': upcode,
                'hname': hname,
                'price': price,
                'sign': sign,
                'change': change,
                'diff': diff,
                'volume': volume,
                'open': open,
                'high': high,
                'low': low,
                'sojinrate': sojinrate,
                'beta': beta,
                'perx': perx,
                'frgsvolume': frgsvolume,
                'orgsvolume': orgsvolume,
                'diff_vol': diff_vol,
                'shcode': shcode,
                'total': total,
                'value': value,
            }
            )
