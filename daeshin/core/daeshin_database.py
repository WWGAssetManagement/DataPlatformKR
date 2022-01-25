from config.settings import DAESHIN_ENGINE, META
from sqlalchemy import Table


class DaeshinDataBase:
    model = None
    table = None
    conn = None

    def __init__(self, model):
        self.model = model
        self.table = self.__get_table(model)
        self.conn = DAESHIN_ENGINE.connect()

    def __get_table(self, model) -> Table:
        return Table(model.__tablename__, META, autoload_with=DAESHIN_ENGINE)

    def _save(self, dict_data: list):
        """
        if you using pandas plz list dict inputs like df.to_dict('records')
        :param dict_data like  [{'col1': 1, 'col2': 0.5}, {'col1': 2, 'col2': 0.75}]
        :return:
        """
        self.conn.execute(self.table.insert().prefix_with("IGNORE"), dict_data)
