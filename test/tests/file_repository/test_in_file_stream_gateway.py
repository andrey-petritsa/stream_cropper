import unittest

import utils
from file_repository.in_file_stream_gateway import InFileStreamGateway
from file_repository.stream_dir import StreamDir
from test.resources import test_stream_dir
from test_helpers.file_helper import FileHelper
from test_helpers.message_builder import MessageBuilder
from test_helpers.stream_builder import StreamBuilder


class TestInFileStreamGateway(unittest.TestCase):
    def setUp(self):
        stream_builder = StreamBuilder()
        stream_builder.build_stream()
        self.stream = stream_builder.get_stream()
        self.message_builder = MessageBuilder()
        utils.stream_dir = StreamDir(test_stream_dir)
        FileHelper.maybe_remove_file(utils.stream_dir.get_path_to_meta_file(self.stream['id']))
        FileHelper.maybe_clean_dir(test_stream_dir)
        self.stream_gateway = InFileStreamGateway()

    def test_save_stream(self):
        self.stream_gateway.save(self.stream)
        saved_stream = self.stream_gateway.find_by_id(self.stream['id'])
        self.assertEqual(saved_stream['name'], 'test-stream')

    def test_date_fields_unserialized(self):
        self.stream_gateway.save(self.stream)
        saved_stream = self.stream_gateway.find_by_id(self.stream['id'])

        self.assertEqual(2011, saved_stream['started_at'].year)

    def test_messages_unserialized(self):
        self.stream_gateway.save(self.stream)
        saved_stream = self.stream_gateway.find_by_id(self.stream['id'])

        first_message = saved_stream['messages'][0]
        second_message = saved_stream['messages'][1]
        distance = first_message.distance(second_message)
        self.assertAlmostEqual(0, distance, 2)

    def test_find_stream_by_id(self):
        self.stream_gateway.save(self.stream)
        saved_stream = self.stream_gateway.find_by_id(self.stream['id'])
        self.assertEqual(saved_stream['name'], 'test-stream')

    def test_find_all_streams(self):
        self.stream_gateway.save(self.stream)
        streams = self.stream_gateway.find_all()
        self.assertEqual(1, len(streams))