import unittest

from interactor.stream_analyzer.message_group_strategy.close_message_group_strategy import CloseMessageGroupStrategy
from interactor.stream_analyzer.moment_finder import MomentFinder
from test_helpers.stream_builder import StreamBuilder


class TestMomentFinder(unittest.TestCase):
    def setUp(self):
        self.finder = MomentFinder(CloseMessageGroupStrategy())
        self.stream_builder = StreamBuilder()
        self.stream_builder.build_stream()


    def test_when_only_one_moment__this_moment_intresting(self):
        self.stream_builder.set_messages('0:0:0')
        stream = self.stream_builder.get_stream()

        moment_radius = 1
        moments = self.finder.find(stream, moment_radius)

        self.assertEqual('00:00:00', str(moments[0]))

    def test_2_messages(self):
        self.stream_builder.set_messages('0:0:0', '0:0:1')
        stream = self.stream_builder.get_stream()

        moment_radius = 1
        moments = self.finder.find(stream, moment_radius)

        self.assertEqual('00:00:00 00:00:01', str(moments[0]))

    def test_all_messages(self):
        self.stream_builder.set_messages('0:0:0', '0:0:1', '0:0:2', "0:1:20")
        stream = self.stream_builder.get_stream()

        moment_radius = 100
        moments = self.finder.find(stream, moment_radius)

        self.assertEqual("00:00:00 00:00:01 00:00:02 00:01:20", str(moments[0]))

    def test_3_messages(self):
        self.stream_builder.set_messages('0:0:0', '0:0:4', '0:0:45')
        stream = self.stream_builder.get_stream()

        moment_radius = 5
        moments = self.finder.find(stream, moment_radius)

        self.assertEqual('00:00:00 00:00:04', str(moments[0]))
        self.assertEqual('00:00:45', str(moments[1]))

    def test_4_messages(self):
        self.stream_builder.set_messages('0:0:0', '0:0:4', '0:0:45', '0:0:49')
        stream = self.stream_builder.get_stream()

        moment_radius = 5
        moments = self.finder.find(stream, moment_radius)

        self.assertEqual('00:00:00 00:00:04', str(moments[0]))
        self.assertEqual('00:00:45 00:00:49', str(moments[1]))

    def test_moment_has_center(self):
        self.stream_builder.set_messages('0:0:0')
        stream = self.stream_builder.get_stream()

        moment_radius = 1
        moments = self.finder.find(stream, moment_radius)

        self.assertEqual('1996-06-25 00:00:00', str(moments[0].get_start()))

    def test_gold(self):
        self.stream_builder.set_messages('0:0:0', '0:0:4', '0:0:25', '0:0:45', '0:0:49', '0:1:49', '0:1:50', '0:1:51', '1:0:49', '1:0:52')
        stream = self.stream_builder.get_stream()

        moment_radius = 5
        moments = self.finder.find(stream, moment_radius)

        self.assertEqual('00:00:00 00:00:04', str(moments[0]))
        self.assertEqual('00:00:25', str(moments[1]))
        self.assertEqual('00:00:45 00:00:49', str(moments[2]))
        self.assertEqual('00:01:49 00:01:50 00:01:51', str(moments[3]))
        self.assertEqual('01:00:49 01:00:52', str(moments[4]))