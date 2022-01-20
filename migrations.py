from daeshin.models.minutepricemodel import MinutePriceModel
from config.settings import DAESHIN_ENGINE

MinutePriceModel.__table__.create(bind=DAESHIN_ENGINE, checkfirst=True)

