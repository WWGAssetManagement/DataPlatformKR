from daeshin.models.minutepricemodel import MinutePriceModel
from ebest.model.stocklistmodel import StockListModel
from ebest.model.sectorcodemodel import SectorCodeModel
from ebest.model.themacodemodel import ThemaCodeModel
from ebest.model.sectorstockmodel import SectorStockModel
from config.settings import DAESHIN_ENGINE, EBEST_ENGINE

MinutePriceModel.__table__.create(bind=DAESHIN_ENGINE, checkfirst=True)


StockListModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
SectorCodeModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
ThemaCodeModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
SectorStockModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
