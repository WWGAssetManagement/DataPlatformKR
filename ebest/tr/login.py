from ebest.core.xa_session import XASession
import os


class Login(XASession):
    __id = None
    __pwd = None
    __cert = None
    __account_password = None
    __url = None

    def __init__(self):
        super().__init__()
        self.__set_login_info()
        self.__request()

    def __set_login_info(self):
        self.__id = os.environ.get("EBEST_ID")
        self.__pwd = os.environ.get("EBEST_PASSWORD")
        self.__cert = os.environ.get("EBEST_CERT")
        self.__account_password = os.environ.get("EBEST_ACCOUNT_PASSWORD")
        self.__url = os.environ.get("EBEST_URL")

    def __request(self):
        self.inst_xa_session.ConnectServer(self.__url, 20001)
        self.inst_xa_session.Login(self.__id, self.__pwd, self.__cert, 0, 0)
        self._receive()

    def get_account(self) -> list:
        num_accounts = self.inst_xa_session.GetAccountListCount()
        return list(map(lambda x: self.__receive_accounts(x), range(num_accounts)))

    def __receive_accounts(self, index):
        return self.inst_xa_session.GetAccountList(index)

    def disconnect(self):
        self.inst_xa_session.DisconnectServer()
