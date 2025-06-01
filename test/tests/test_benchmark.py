import unittest

import utils
from mocks.logger.spy_logger import SpyLogger
from utils.benchmark.benchmark import Benchmark


class ImportantClass(unittest.TestCase):
    def callback(self):
        a = 0
        b = 2
        return b

class TestBenchmark(unittest.TestCase):
    def setUp(self):
        self.benchmark = Benchmark()
        self.logger = SpyLogger()
        utils.logger = SpyLogger()

    def tearDown(self):
        pass

    def test_noth(self):
        pass

    def test_callback_logged(self):
        obj = ImportantClass()
        response = self.benchmark.run(obj.callback, 'ImportantClass::callback')
        self.assertNotEqual("123", self.logger.info_messages[0])
        self.assertEqual(2, response)

