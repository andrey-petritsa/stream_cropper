import unittest

import interactor.factories
import utils
from gui.stream_presenter import StreamPresenter
from mocks.interactor.in_memory_gateway_factory import InMemoryGatewayFactory
from mocks.logger.spy_logger import SpyLogger
from utils.benchmark.benchmark import Benchmark
from utils.benchmark.show_all_stream_info_command_benchmark import ShowAllStreamInfoCommandBenchmark


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

    def test_decorator(self):
        interactor.factories.gateway_factory = InMemoryGatewayFactory()
        decorator = ShowAllStreamInfoCommandBenchmark(StreamPresenter())
        decorator.execute()

        self.assertEqual("ImportantClass::callback Took 0.0 seconds", self.logger.info_messages[0])

