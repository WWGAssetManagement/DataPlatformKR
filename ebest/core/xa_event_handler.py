from ebest.settings import LOG


class XASessionEventHandler:
    status = False

    def OnLogin(self, code, msg):
        LOG.logger.log(f"OnLogin: {code}, {msg}")

    def OnLogout(self):
        LOG.logger.log("Logout")

    def OnDisconnect(self):
        LOG.logger.log("Disconnect")
