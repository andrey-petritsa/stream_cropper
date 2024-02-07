import unittest

import utils
from mocks.logger.spy_logger import SpyLogger
from test_helpers.twith_stream_finder import TwithStreamFinder


class TestTwithStreamFinder(unittest.TestCase):
    def test_find(self):
        utils.logger = SpyLogger()

        finder = TwithStreamFinder()
        stream_reference = finder.find_online_stream()
        self.assertNotEqual(None, stream_reference)