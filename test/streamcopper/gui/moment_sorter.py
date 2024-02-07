import unittest

from gui.moment_sorter import MomentSorter
from mocks.interactor.moment_stub import MomentStub
from test_helpers.stream_builder import StreamBuilder


class TestMomentSorter(unittest.TestCase):
    def setUp(self):
        self.moment_sorter = MomentSorter()
        self.stream_builder = StreamBuilder()

    def tearDown(self):
        pass

    def test_sorting(self):
        stream = self.stream_builder.get_stream()
        stream['moments'] = [
            MomentStub(1, '2011-11-04T12:00:00'),
            MomentStub(4, '2011-11-04T12:01:00'),
        ]

        sorted_stream = self.moment_sorter.sort_by_weights_ask(stream)

        self.assertEqual("weight: 4", str(sorted_stream['moments'][0]))
