import unittest

import utils
from mocks.platform.stub_check_online_strategy import StubCheckOnlineStrategy
from refactor.fake_id_generator import FakeIdGenerator
from refactor.web.mock.stub_web_client import StubWebClient
from twith_platform.twith.twith import Twith
from utils import RequestsClient


class TestTwith(unittest.TestCase):
    def setUp(self):
        utils.id_generator= FakeIdGenerator()
        utils.web_client = StubWebClient()
        self.check_online_strategy = StubCheckOnlineStrategy()
        self.twith = Twith(self.check_online_strategy)

    def tearDown(self):
        utils.web_client = RequestsClient()

    def read_stream_online_page(self):
        f = open("resources/streamer_online.html", "r")
        content = f.read()
        f.close()
        return content

    def read_stream_offline_page(self):
        f = open("resources/streamer_offline.html", "r")
        content = f.read()
        f.close()
        return content

    def download_online_stream(self, stream_reference):
        utils.web_client.response = self.read_stream_online_page()
        self.check_online_strategy.is_online_response = True
        return self.twith.download_stream(stream_reference)

    def download_offline_stream(self, stream_reference):
        utils.web_client.response = self.read_stream_offline_page()
        self.check_online_strategy.is_online_response = False
        return self.twith.download_stream(stream_reference)

    def test_download_online_stream(self):
        stream = self.download_online_stream("bigrussianmum")

        self.assertEqual("КООП_Hunt_Showdown_с_revolt_BIGRUSSIANBR0_и_BRM__БХП_КЛИПЫ_РАСПИСАНИЕ", stream['name'])
        self.assertEqual(True, stream['is_online'])
        self.assertTrue('bigrussianmum' in stream['id'])

    def test_download_offline_stream(self):
        stream = self.download_offline_stream("bigrussianmum")

        self.assertEqual("stream offline", stream['name'])
        self.assertEqual(False, stream['is_online'])

