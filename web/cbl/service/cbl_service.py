from common.util.db_util import DBManager, SqlType


class CBlService:
    def __init__(self):
        self.db = DBManager()

    def get_cbl_as_date(self, json_param):
        """
        명령 날짜에 해당하는 0시 ~ 23시 cbl 가져옴
        :param json_param: command_date 포함
        :return: db_util에서 쿼리 실행
        """
        command_date = json_param.get('command_date')
        sql = f'''
            SELECT DATE_FORMAT(CBL_TIME, '%Y-%m-%d %T') AS CBL_TIME,
               ROUND(MID610, 2) AS MID610,
               ROUND(MID46, 2) AS MID46,
               ROUND(MID810, 2) AS MID810
            FROM DR_SCBL
            WHERE CBL_TIME LIKE CONCAT('{command_date}', '%')
        '''
        ret = self.db.execute_query(sql, SqlType.SELECT)

        if ret is None or len(ret) == 0:
            return None

        return ret

    def set_hist_data(self, json_param):
        """
        history data insert
        :param json_param: insert할 data
        :return: db_util에서 쿼리 실행
        """
        try:
            sql = '''
            INSERT INTO DR_USE_HIST60(HIST_TIME, DELT_VAL)
            '''
            update_sql = '''
            ON DUPLICATE KEY UPDATE HIST_TIME = VALUES(HIST_TIME), DELT_VAL = VALUES(DELT_VAL)
            '''
            for d in json_param:
                sql += f'''
                SELECT '{d["HIST_TIME"]}', {d["DELT_VAL"]} UNION
                '''
            sql = sql[:-23] + update_sql
            return self.db.execute_query(sql, SqlType.INSERT)
        except Exception as e:
            print(e.__getstate__())
            return -1
