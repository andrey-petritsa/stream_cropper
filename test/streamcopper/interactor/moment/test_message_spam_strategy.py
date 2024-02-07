import unittest

from interactor.stream_analyzer.message_group_strategy.message_spam_strategy import MessageSpamStrategy
from interactor.stream_analyzer.moment_finder import MomentFinder
from test_helpers.stream_builder import StreamBuilder


class TestMessageSpamStrategy(unittest.TestCase):
    def setUp(self):
        self.finder = MomentFinder(MessageSpamStrategy())
        self.stream_builder = StreamBuilder()
        self.stream_builder.build_stream()

    def find_moments(self, stream):
        moments = self.finder.find(stream, 1)
        string_moments = self.convert_moments_to_string(moments)
        return string_moments

    def convert_moments_to_string(self, moments):
        string_moments = []
        for moment in moments:
            string_moments.append(str(moment))
        return ','.join(string_moments)

    def test_no_groups(self):
        self.stream_builder.set_messages()
        stream = self.stream_builder.get_stream()
        self.assertEqual("", self.find_moments(stream))

    def test_one_message(self):
        self.stream_builder.set_messages('0:0:0')
        stream = self.stream_builder.get_stream()
        self.assertEqual("00:00:00", self.find_moments(stream))

    def test_two_messages(self):
        self.stream_builder.set_messages('0:0:0', '0:0:1')
        stream = self.stream_builder.get_stream()
        self.assertEqual("00:00:00 00:00:01", self.find_moments(stream))

    def test_two_messages_two_groups(self):
        self.stream_builder.set_messages('0:0:0', '0:0:25')
        stream = self.stream_builder.get_stream()
        self.assertEqual("00:00:00,00:00:25", self.find_moments(stream))

    def test_three_messages_three_groups(self):
        self.stream_builder.set_messages('0:0:0', '0:0:25', '0:0:50')
        stream = self.stream_builder.get_stream()
        self.assertEqual("00:00:00,00:00:25,00:00:50", self.find_moments(stream))

    def test_4_message_2_groups(self):
        self.stream_builder.set_messages('0:0:0', '0:0:1', '0:0:50', '0:0:51')
        stream = self.stream_builder.get_stream()
        self.assertEqual("00:00:00 00:00:01,00:00:50 00:00:51", self.find_moments(stream))

    def test_gold(self):
        self.stream_builder.set_messages('0:0:0', '0:0:1', '0:0:3', '0:0:5', "0:0:6", '0:0:50', '0:0:51')
        stream = self.stream_builder.get_stream()
        self.assertEqual("00:00:00 00:00:01,00:00:03,00:00:05 00:00:06,00:00:50 00:00:51", self.find_moments(stream))