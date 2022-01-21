import win32com.client
import pythoncom
from ebest.core.xa_query_events_handler import XAQeuryEventsHandler
from constants import BASE_DIR


class XAQueryEvents:
    query = None
    tr_code = None
    inblock = None
    outblock = None
    outblock1 = None
    res_file_dir = None

    def __init__(self, tr_code):
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQeuryEventsHandler)
        self.tr_code = tr_code
        self._set_inblock_name()
        self._set_outblock_name()
        self._set_outblock1_name()
        self._set_res_file_dir()
        self._load_from_resfile()

    def _set_inblock_name(self):
        self.inblock = f"{self.tr_code}InBlock"

    def _set_outblock_name(self):
        self.outblock = f"{self.tr_code}OutBlock"

    def _set_outblock1_name(self):
        self.outblock1 = f"{self.tr_code}OutBlock1"

    def _set_res_file_dir(self):
        self.res_file_dir = f"{BASE_DIR}\\Res\\{self.tr_code}.res"

    def _load_from_resfile(self):
        self.query.LoadFromResFile(self.res_file_dir)

    def _receive(self):
        while XAQeuryEventsHandler.status == False:
            pythoncom.PumpWaitingMessages()
        XAQeuryEventsHandler.status = False

    def _request(self, bNext='0'):
        # 0이면 조회 1이면 다음 조회
        self.query.Request(bNext)

    def _set_field_data(self, szBlockName, szFieldName, nOccursIndex, szData):
        # E.g) szBlockName: t1820InBlock, szFieldName: shcode, nOccursIndex: 0, szData: 005930
        self.query.SetFieldData(szBlockName, szFieldName, nOccursIndex, szData)

    def _get_block_count(self, outblock):
        return self.query.GetBlockCount(outblock)

    def _get_field_data(self, outblock, szFieldName, nOccursIndex) -> str:
        return self.query.GetFieldData(outblock, szFieldName, nOccursIndex).strip()
