import unittest
from datetime import datetime



class YoutubeChatProviderTest(unittest.TestCase):
    def test_get_info(self):
        provider = YoutubeChatProvider()

        info = provider.get_stream_info('maZ2qjF5YgM')

        self.assertEqual(info['first_message'].datetime, datetime(2023, 9, 30, 15, 50, 22, 696495))

