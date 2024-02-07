import unittest

from test_helpers.stream_builder import StreamBuilder
from utils import StreamIdGenerator


class TestStreamIdGenerator(unittest.TestCase):
    def setUp(self):
        self.stream_id_generator = StreamIdGenerator()

    def test_generate(self):
        stream_builder = StreamBuilder()
        stream_builder.build_stream()
        stream = stream_builder.get_stream()
        id = self.stream_id_generator.generate(stream)

        self.assertEqual("acrosspaper-2011-11-04.12-00-00", id)
