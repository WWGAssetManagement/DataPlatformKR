from daeshin.models.models import MinutePriceModel
from ebest.model.models import (
    ManagementInsincerityInvestmentPrecautionsModel,
    SectorStockModel,
    SectorCodeModel,
    StockListModel,
    ThemaCodeModel,
    InvestWarningSupensionTradeLiquidatedTradeModel
)
from config.settings import DAESHIN_ENGINE, EBEST_ENGINE

MinutePriceModel.__table__.create(bind=DAESHIN_ENGINE, checkfirst=True)


StockListModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
SectorCodeModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
ThemaCodeModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
SectorStockModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
ManagementInsincerityInvestmentPrecautionsModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)
InvestWarningSupensionTradeLiquidatedTradeModel.__table__.create(bind=EBEST_ENGINE, checkfirst=True)