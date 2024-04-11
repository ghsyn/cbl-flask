import datetime
import logging


class Model:
    def __init__(self):
        pass  # 특별히 초기화 필요 없음.

    def __str__(self):
        return f'{self.id}'

    def __repr__(self):
        return f'{self.id}'

    def append_variable(self, name, val):
        setattr(self, name, val)


class Log:
    def __init__(self, __name__):
        # 로거 설정
        self.logger = logging.getLogger(__name__)
        self.name = __name__

    def make_logger(self):
        # 일반, 크리티컬 이벤트에 대한 포매터 생성
        formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
        formatter_critical = logging.Formatter("!!![CRITICAL EVENT] %(asctime)s %(levelname)s:%(message)s")

        # 콘솔 및 파일에 대한 핸들러 세팅
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler('./log/{}_{}.log'.format(self.name, datetime.datetime.now().strftime('%y%m%d')), encoding='utf-8')

        # 각 핸들러에 레벨 및 포매터 세팅
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        file_handler.setLevel(logging.CRITICAL)
        file_handler.setFormatter(formatter_critical)

        # 각 핸들러를 로거에 추가
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

        return self.logger
