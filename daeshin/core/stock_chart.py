import win32com.client


class StockChart:
    inst_cp_stock_chart = None

    def __init__(self):
        self.inst_cp_stock_chart = win32com.client.Dispatch("CpSysDib.StockChart")
        self.is_connect()

    def is_connect(self):
        instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
        print(instCpCybos.IsConnect)

    def set_input_value(self, type, value):
        self.inst_cp_stock_chart.SetInputValue(type, value)

    def block_request(self):
        self.inst_cp_stock_chart.BlockRequest()

    def get_header_value(self, type):
        return self.inst_cp_stock_chart.GetHeaderValue(type)

    def get_data_value(self, type, index):
        return self.inst_cp_stock_chart.GetDataValue(type, index)
