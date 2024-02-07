import unittest

import utils
from file_repository.stream_dir import StreamDir
from interactor.convert_video_to_hls_observer import ConvertVideoToHlsObserver
from mocks.interactor.record_video_spy_task import RecordVideoSpyTask
from mocks.logger.spy_logger import SpyLogger
from slow import test_stream_dir
from test_helpers.file_helper import FileHelper


class TestConvertVideoToHlsObserver(unittest.TestCase):
    def setUp(self):
        utils.logger = SpyLogger()

    def tearDown(self):
        FileHelper.maybe_remove_dir('resources/streams/example_stream/hls')
        FileHelper.maybe_remove_dir('/var/hls/example_stream')
        utils.stream_dir = StreamDir(test_stream_dir)

    def test_update(self):
        observer = ConvertVideoToHlsObserver()
        spy_task = RecordVideoSpyTask()
        spy_task.stream['id'] = 'example_stream'
        utils.stream_dir = StreamDir('resources/streams')

        observer.update(spy_task)

        self.assertTrue(FileHelper.is_dir_exists('/var/hls/example_stream'))
        self.assertTrue(FileHelper.is_file_exists('/var/hls/example_stream/video.m3u8'))

