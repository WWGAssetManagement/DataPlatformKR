from daeshin.type import *
from daeshin.models.models import MinutePriceModel
from daeshin.core.stock_chart import StockChart
from datetime import datetime
from daeshin.utils.format import Format
from daeshin.core.daeshin_database import DaeshinDataBase


class MinutePrice(DaeshinDataBase):
    stock_chart = None
    results = None
    ticker = None

    def __init__(self):
        self.stock_chart = StockChart()
        DaeshinDataBase.__init__(self, MinutePriceModel)

    def set(self, code, start, end):
        self.ticker = code
        code = Format.get_code(code)
        self.stock_chart.set_input_value(SetInputValue.CODE.value, code)
        self.stock_chart.set_input_value(SetInputValue.GUBUN.value, Gubun.REQUEST_FOR_PERIOD.value)
        self.stock_chart.set_input_value(SetInputValue.END_DATE.value, end)
        self.stock_chart.set_input_value(SetInputValue.START_DATE.value, start)
        self.stock_chart.set_input_value(SetInputValue.FIELD.value, (
            Field.DATE.value,
            Field.TIME.value,
            Field.OPEN_PRICE.value,
            Field.HIGH_PRICE.value,
            Field.LOW_PRICE.value,
            Field.CLOSE_PRICE.value,
            Field.VOLUME.value,
            Field.TRANSACTION_AMOUNT.value
        ))
        self.stock_chart.set_input_value(SetInputValue.CHART_GUBUN.value, ChartGubun.MINUTE.value)
        self.stock_chart.block_request()
        self.results = self.__get()
        return self

    def __get(self) -> list:
        index_number = self.stock_chart.get_header_value(GetHeaderValue.RECEIVE_NUMBER.value)
        return list(map(lambda x: self.__get_row(x), range(index_number)))

    def to_sql(self):
        print(len(self.results))
        self._save(dict_data=self.results)

    def __get_row(self, index) -> dict:
        date = self.stock_chart.get_data_value(0, index)
        time = self.stock_chart.get_data_value(1, index)
        open_price = self.stock_chart.get_data_value(2, index)
        high_price = self.stock_chart.get_data_value(3, index)
        low_price = self.stock_chart.get_data_value(4, index)
        close_price = self.stock_chart.get_data_value(5, index)
        volume = self.stock_chart.get_data_value(6, index)
        transation_amount = self.stock_chart.get_data_value(7, index)

        date_time = datetime.strptime(f"{date} {time}", '%Y%m%d %H%M')
        return {'date': date_time, 'ticker': self.ticker, 'open': open_price, 'high': high_price, 'low': low_price,
                'close': close_price, 'volume': volume, 'transaction_amount': transation_amount
                }
