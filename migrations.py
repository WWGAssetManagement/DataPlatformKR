from daeshin.models.minutepricemodel import MinutePriceModel
from ebest.model.stocklistmodel import StockListModel
from config.settings import DAESHIN_ENGINE, EBEST_ENGINE

MinutePriceModel.__table__.create(bind=DAESHIN_ENGINE, checkfirst=True)
StockListModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
