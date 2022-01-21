from ebest.settings import LOG


class XAQeuryEventsHandler:
    status = False

    def OnReceiveData(self, szTrCode):
        LOG.logger.debug(f"OnReceiveData: {szTrCode}")
        XAQeuryEventsHandler.status =  True

    def OnReceiveMessage(self, systemError, messageCode, message):
        LOG.logger.debug(f"OnReceiveMessage : {systemError}{messageCode}{message}")
