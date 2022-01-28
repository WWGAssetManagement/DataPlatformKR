from .api import (
    API,
    CorpCodes,
    DartListDateEx,
    DartList
)


def get_api(idx):
    return API(idx)


def get_corp_codes(idx=0):
    return CorpCodes(idx)


def get_dart_list_date_ex(date, idx=0):
    return DartListDateEx(date, idx)


def get_dart_list(corp=None, start=None, end=None, kind='', kind_detail='', final=True, idx=0):
    return DartList(corp, start, end, kind, kind_detail, final, idx)
