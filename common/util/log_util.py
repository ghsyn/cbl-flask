import sys
from _datetime import datetime
import logging
from pathlib import Path


class LogUtil:
    def __init__(self, name):
        # 로거 설정
        self.logger = logging.getLogger(name)
        self.name = name

    def make_logger(self):
        #  출력별 Handler 생성
        handler_stream = logging.StreamHandler()
        handler_file = logging.FileHandler(
            filename='../../logs/{}_{}.log'.format(self.name, datetime.now().strftime('%y%m')),
            encoding='utf-8'
        )

        # # Handler별 로깅 레벨 지정
        handler_stream.setLevel(level=logging.DEBUG)
        handler_file.setLevel(level=logging.CRITICAL)

        # # 포맷 객체 생성
        formatter_stream = logging.Formatter(fmt='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        formatter_file = logging.Formatter(fmt='[%(asctime)s] %(levelname)-8s [%(filename)s:%(lineno)d]  %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 핸들러별 포맷 설정
        handler_stream.setFormatter(formatter_stream)
        handler_file.setFormatter(formatter_file)

        # 각 핸들러를 로거에 추가
        self.logger.addHandler(handler_stream)
        self.logger.addHandler(handler_file)

        return self.logger
