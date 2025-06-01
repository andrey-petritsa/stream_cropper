import unittest

import utils
from interactor.use_cases.convert_video_to_hls_command import ConvertVideoToHlsCommand
from mocks.logger.spy_logger import SpyLogger
from test_helpers.file_helper import FileHelper


class TestConvertVideoToHlsCommand(unittest.TestCase):
    def setUp(self):
        utils.logger = SpyLogger()

    def tearDown(self):
        FileHelper.maybe_remove_dir('resources/video')
        FileHelper.maybe_remove_dir('/var/hls/example_stream')

    def test_execute(self):
        command = ConvertVideoToHlsCommand()
        command.execute('resources/video/video.mp4')
        self.assertTrue(FileHelper.is_dir_exists('resources/video/hls'))

