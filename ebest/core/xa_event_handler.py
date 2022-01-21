from ebest.settings import LOG


class XASessionEventHandler:
    status = False

    def OnLogin(self, code, msg):
        LOG.logger.debug(f"OnLogin: {code}, {msg}")
        XASessionEventHandler.status = True

    def OnLogout(self):
        LOG.logger.debug("Logout")

    def OnDisconnect(self):
        LOG.logger.debug("Disconnect")
