import win32com.client
import pythoncom
from ebest.core.xa_event_handler import XASessionEventHandler


class XASession:
    inst_xa_session = None

    def __init__(self):
        self.inst_xa_session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)

    def _receive(self):
        while XASessionEventHandler.status == False:
            pythoncom.PumpWaitingMessages()
