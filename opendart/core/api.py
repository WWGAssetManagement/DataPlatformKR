import OpenDartReader
import pandas as pd

from config.settings import (
    OPENDARTAPI_1,
    OPENDARTAPI_2,
    OPENDARTAPI_3,
    OPENDARTAPI_4,
)
from opendart.model.models import CorpCodesModel, DartListDateExModel, DartListModel
from opendart.core.opendart_database import OpenDartDatabase


class API(OpenDartDatabase):
    __api_keys = []
    api = None
    results = None

    def __init__(self, idx: int):
        self.__api_keys = [
            OPENDARTAPI_1,
            OPENDARTAPI_2,
            OPENDARTAPI_3,
            OPENDARTAPI_4,
        ]
        self.api = self.__get_api(idx)

    def get(self):
        return self.api

    def set(self, results: pd.DataFrame, model):
        self.results = results
        super().__init__(model)

    def __get_api(self, idx):
        i = idx % len(self.__api_keys)
        return OpenDartReader(self.__api_keys[i])

    def to_mysql(self):
        self._save(self.results.to_dict('records'))
        del self.conn

    def to_pandas(self):
        return self.results


class CorpCodes(API):
    def __init__(self, idx):
        super().__init__(idx)
        results = self.api.corp_codes
        self.set(results=results, model=CorpCodesModel)


class DartListDateEx(API):
    def __init__(self, date: str, idx: int):
        super().__init__(idx)
        results = self.api.list_date_ex(date)
        self.set(results, DartListDateExModel)


class DartList(API):
    def __init__(self, corp=None, start=None, end=None, kind='', kind_detail='', final=True, idx=0):
        super().__init__(idx)
        results = self.api.list(corp, start, end, kind, kind_detail, final)
        if 'rcept_dt' in results.columns:
            results['rcept_dt'] = pd.to_datetime(results['rcept_dt'])
        self.set(results, DartListModel)
