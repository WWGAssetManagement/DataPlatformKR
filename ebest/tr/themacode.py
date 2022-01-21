"""
Thema Code 등록
"""
from ebest.core.xa_query_events import XAQueryEvents
from ebest.core.ebest_database import EbestDataBase
from ebest.model.themacodemodel import ThemaCodeModel


class ThemaCode(XAQueryEvents, EbestDataBase):
    tr_code = "t8425"
    results = None

    def __init__(self):
        XAQueryEvents.__init__(self, tr_code=self.tr_code)
        EbestDataBase.__init__(self, model=ThemaCodeModel)
        self._set_field_data(self.inblock, "dummy", 0, "0")
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

    def __get_row(self, index):
        tmcode = self._get_field_data(self.outblock, 'tmcode', index).strip()
        tmname = self._get_field_data(self.outblock, 'tmname', index).strip()
        return {
            "tmcode": tmcode,
            "tmname": tmname
        }
