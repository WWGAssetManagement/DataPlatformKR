from enum import Enum


class ChartGubun(Enum):
    DAY = ord('D')
    WEEK = ord('W')
    MONTH = ord('M')
    MINUTE = ord('m')
    TICK = ord('T')


class Field(Enum):
    DATE = 0
    TIME = 1
    OPEN_PRICE = 2
    HIGH_PRICE = 3
    LOW_PRICE = 4
    CLOSE_PRICE = 5
    DIFF = 6
    VOLUME = 8
    TRANSACTION_AMOUNT = 9
    CUM_MEDO_QUANTITY = 10
    CUM_MESU_QUANTITY = 11


class GapAdjust(Enum):
    TRUE = ord('1')
    FALSE = ord('0')


class PriceAdjust(Enum):
    TRUE = ord('1')
    FALSE = ord('0')


class Volume(Enum):
    OVERTIME_TRANSACTION = ord('1')


class SetInputValue(Enum):
    CODE = 0
    GUBUN = 1
    END_DATE = 2
    START_DATE = 3
    REQUEST_NUMBER = 4
    FIELD = 5
    CHART_GUBUN = 6
    FREQUENCY = 7
    GAP_ADJ = 8
    ADJ_PRICE = 9
    VOLUME_GUBUN = 10


class GetHeaderValue(Enum):
    CODE = 0
    FIELD_NUMBER = 1
    FIELD_ARRAY = 2
    RECEIVE_NUMBER = 3

class Gubun(Enum):
    REQUEST_FOR_PERIOD = ord('1')
    REQUEST_FOR_NUMBER = ord('2')