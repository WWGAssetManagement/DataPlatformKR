from ebest.settings import LOG


class XAQeuryEvents:
    status = False

    def OnReceiveData(self, szTrCode):
        LOG.logger.log(f"OnReceiveData: {szTrCode}")

    def OnReceiveMessage(self, systemError, messageCode, message):
        LOG.logger.log(f"OnReceiveMessage : {systemError}{messageCode}{message}")
