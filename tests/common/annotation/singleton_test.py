from unittest import TestCase

from common.util.db_util import DBManager


class TestSingleton(TestCase):
    def test_singleton(self):
        db1 = DBManager()
        db2 = DBManager()
        self.assertEqual(db1, db2)
