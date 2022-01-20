import win32com.client
import pythoncom
from src.xa_query_events.xa_query_events import XAQueryEvents
from constants import BASE_DIR


class XAQueryEventsBase:
    query = None
    __tr_code = None
    inblock = None
    outblock = None
    outblock1 = None
    res_file_dir = None

    def __init__(self, tr_code):
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
        self.__tr_code = tr_code
        self._set_inblock_name()
        self._set_outblock_name()
        self._set_outblock1_name()
        self._set_res_file_dir()
        self._load_from_resfile()

    def _set_inblock_name(self):
        self.inblock = f"{self.__tr_code}InBlock"

    def _set_outblock_name(self):
        self.outblock = f"{self.__tr_code}OutBlock"

    def _set_outblock1_name(self):
        self.outblock1 = f"{self.__tr_code}OutBlock1"

    def _set_res_file_dir(self):
        self.res_file_dir = f"{BASE_DIR}\\Res\\{self.__tr_code}.res"

    def _load_from_resfile(self):
        self.query.LoadFromResFile(self.res_file_dir)

    def receive(self):
        while XAQueryEvents.status == False:
            pythoncom.PumpWaitingMessages()
        XAQueryEvents.status = False

    def request(self, bNext='0'):
        # 0이면 조회 1이면 다음 조회
        self.query.Request(bNext)

    def set_field_data(self, szBlockName, szFieldName, nOccursIndex, szData):
        # szBlockName: e.g t1820InBlock, szFieldName: e.g shcode, nOccursIndex e.g 0, szData e.g 005930
        self.query.SetFieldData(szBlockName, szFieldName, nOccursIndex, szData)

    def get_block_count(self, outblock):
        return self.query.GetBlockCount(outblock)

    def get_field_data(self, outblock, szFieldName, nOccursIndex) -> str:
        return self.query.GetFieldData(outblock, szFieldName, nOccursIndex).strip()
