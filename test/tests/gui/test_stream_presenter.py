import unittest

from gui.stream_presenter import StreamPresenter
from test_helpers.message_builder import MessageBuilder
from test_helpers.stream_builder import StreamBuilder


class TestStreamPresenter(unittest.TestCase):
    def setUp(self):
        self.message_builder = MessageBuilder()
        self.presenter = StreamPresenter()
        self.stream_builder = StreamBuilder()

    def format_stream(self):
        stream = self.create_anon_stream()
        view_stream = self.presenter.format(stream)
        return view_stream

    def create_anon_stream(self):
        self.stream_builder.build_stream()
        self.stream_builder.set_moments()
        stream = self.stream_builder.get_stream()

        return stream

    def test_format_stream(self):
        stream = self.format_stream()
        self.assertEqual('test-stream', stream['name'])

    def test_format_stream_date(self):
        stream = self.format_stream()
        self.assertEqual("2011-11-04 12:00:00", stream['started_at'])
        self.assertEqual("2011-11-04 12:05:23", stream['messages'][0]['datetime'])

    def test_fist_moment_has_weight(self):
        stream = self.format_stream()
        first_moment = stream['moments'][0]

        self.assertEqual("4", first_moment['weight'])

    def test_first_moment_center_start_from_stream_start(self):
        stream = self.format_stream()
        first_moment = stream['moments'][0]
        second_moment = stream['moments'][1]

        self.assertEqual('0:01:15', first_moment['delta']['start'])
        self.assertEqual('0:00:00', second_moment['delta']['start'])
        self.assertEqual('2011-11-04 12:00:00', second_moment['start'])

    def test_moment_has_sec_delta(self):
        stream = self.format_stream()
        first_moment = stream['moments'][0]

        self.assertEqual('75.0', first_moment['delta_sec']['start'])
        self.assertEqual('75.0', first_moment['delta_sec']['end'])

