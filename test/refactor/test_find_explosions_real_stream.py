import sys
import unittest

from interactor.stream_analyzer.weight_builder import WeightBuilder
from streamcropper.interactor.stream_analyzer.stream_analyzer import StreamAnalyzer


class FindExplosionsRealStreamTest(unittest.TestCase):
    def test_find_explosions_in_real_youtube_video(self):
        sys.setrecursionlimit(100000)
        analyzer = StreamAnalyzer(YoutubeChatProvider(), WeightBuilder())

        analyze = analyzer.analyze_stream('E0A8-cw97gs', 10)

        self.assertEqual(9, analyze[28]['weight'])
