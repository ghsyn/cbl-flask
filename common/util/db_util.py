from pymysql.cursors import DictCursor
from sqlalchemy import create_engine, text, Subquery, RowMapping, select, MetaData, Table, Column, String, Double, DateTime
from sqlalchemy.orm import sessionmaker

from common.annotation.singleton import singleton
from common.config.global_config import GlobalConfig
from common.util.common_util import Log
from enum import Enum


class SqlType(Enum):
    SELECT = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4

@singleton
class DBManager:
    def __init__(self):
        # self.logger = Log("DBManager").make_logger()
        self.prop = GlobalConfig('properties.ini').read_config()["DB"]

        self.engine = create_engine('mysql+pymysql://{user}:{password}@{host}/{db_name}?charset={charset}'.format(
            user=self.prop['user'],
            password=self.prop['password'],
            host=self.prop['host'],
            db_name=self.prop['db_name'],
            charset=self.prop['charset']),
            execution_options={
                'autocommit': True,
                'pool_pre_ping': True,
                'pool_recycle': 3600,
                'pool_size': 10,
            })
        self.session = sessionmaker(bind=self.engine)

    def execute_query(self, query, sql_type: SqlType):
        """
        쿼리 실행 함수
        :param query: 실행할 쿼리
        :param sql_type: 쿼리 유형
        :return: 실행 결과 값 (dict or int)
        """
        session = self.session()
        try:
            if sql_type == SqlType.SELECT:
                con = session.connection()
                with con.connection.cursor(DictCursor) as cursor:
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    return rows
            else:
                res = session.connection().execute(text(query))
                session.commit()
                return res.rowcount
        except Exception as e:
            session.rollback()
            return -1
        finally:
            session.close()