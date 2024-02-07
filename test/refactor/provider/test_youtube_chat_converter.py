import unittest



class YoutubeChatProviderTest(unittest.TestCase):
    def test_convert(self):
        id = '8103dlfCdFY'
        converter = YoutubeMessageConverter()

        message = converter.convert(youtubeMessages[0])

        self.assertEqual('ВиРагý', message['user']['name'])
        self.assertEqual('unknown', message['user']['role'])

