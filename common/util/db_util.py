import os
from typing import Sequence

from sqlalchemy import create_engine, text, RowMapping
from sqlalchemy.orm import sessionmaker

from common.util.common_util import Log

_select_str = "SELECT * FROM"
_where_str = " WHERE "
_ord_str = " ORDER BY "
_limit_str = " LIMIT "

# os.putenv('MARIA_DB_USER', 'root')
# os.putenv('MARIA_DB_PASSWORD', '1q2w3e4r!')
# os.putenv('MARIA_DB_HOST', 'localhost')
# os.putenv('MARIA_DB_NAME', 'elt_dr')
#
# user = os.getenv('MARIA_DB_USER')
# password = os.getenv('MARIA_DB_PASSWORD')
# host = os.getenv('MARIA_DB_HOST')
# name = os.getenv('MARIA_DB_TABLE_NAME')

class DBManager:

    def __init__(self):
        self.logger = Log("DBManager").make_logger()

        # TODO: db 정보 저장 방법 최적화
        # self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{name}?charset=utf8', echo=True)
        self.engine = create_engine('mysql+pymysql://root:1q2w3e4r!@localhost/elt_dr?charset=utf8', echo=True)
        self.session_factory = sessionmaker(bind=self.engine)

    def __execute_sql(self, sql):
        try:
            self.engine = self.session_factory()
            print(sql)
            return self.engine.execute(text(sql)).mappings().fetchall()
        except Exception as e:
            self.engine.rollback()
            self.logger.error(e)
        finally:
            self.engine.close()

    def select_all(self, table, where=None, order=None, limit=None):
        sql = "{} {}".format(_select_str, table)
        if where:
            sql += _where_str + where
        if order:
            sql += _ord_str + order
        if limit:
            sql += _limit_str + str(limit)
        return self.__execute_sql(sql)

    '''
    **kwargs = [HIST_TIME='%Y-%m-%d %T',DELT_VAL=None]
    '''
    def select_for_date_format(self, table, **kwargs) -> Sequence[RowMapping]:
        try:
            if kwargs.__len__() == 0:
                self.logger.error("column is empty")
                return {}
            cols = ""

            for key, value in kwargs.items():
                if value is None:
                    cols += key + ", "
                elif value is not None:
                    if not isinstance(value, str):
                        value = "\'{}\'".format(str(value))
                    cols += "DATE_FORMAT({}, '{}') AS {}, ".format(key, value, key)

            cols = cols[:-2]
            sql = "SELECT " + cols + " FROM " + table + ";"
            print(sql)
            result = self.__execute_sql(sql)
            return result
        except Exception as e:
            self.logger.error(e)
