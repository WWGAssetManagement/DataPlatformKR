"""
StockList: 주식종목조회
"""
from ebest.core.xa_query_events import XAQueryEvents
from datetime import datetime


class StockList(XAQueryEvents):
    tr_code = "t8430"

    def __init__(self):
        super().__init__(tr_code=self.tr_code)

    def set(self):
        self.set_field_data(self.inblock, "gubun", 0, 0)
        self.request()
        self.receive()

    def get(self) -> list:
        index_num = self.get_block_count(self.outblock)
        return list(map(lambda x: self.__get_row(x), range(index_num)))

    def __get_row(self, index) -> dict:
        date = datetime.now()
        hname = self.get_field_data(self.outblock, 'hname', index).strip()
        shcode = self.get_field_data(self.outblock, 'shcode', index).strip()
        expcode = self.get_field_data(self.outblock, "expcode", index).strip()
        etfgubun = int(self.get_field_data(self.outblock, "etfgubun", index).strip())
        uplmtprice = int(self.get_field_data(self.outblock, "uplmtprice", index).strip())
        dnlmtprice = int(self.get_field_data(self.outblock, "dnlmtprice", index).strip())
        jnilclose = int(self.get_field_data(self.outblock, "jnilclose", index).strip())
        memedan = int(self.get_field_data(self.outblock, "memedan", index).strip())
        recprice = int(self.get_field_data(self.outblock, "recprice", index).strip())
        gubun = int(self.get_field_data(self.outblock, "gubun", index).strip())

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
