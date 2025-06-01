import time
import unittest

import utils
from file_repository.stream_dir import StreamDir
from main.app_factory import AppFactory
from test.resources import test_stream_dir
from test_helpers.file_helper import FileHelper
from test_helpers.twith_stream_finder import TwithStreamFinder
from utils import StdoutLogger


class TestRecordVideoTask(unittest.TestCase):
    def setUp(self):
        utils.stream_dir = StreamDir(test_stream_dir)
        FileHelper.maybe_clean_dir(test_stream_dir)
        utils.logger = StdoutLogger()

        self.finder = TwithStreamFinder()
        self.factory = AppFactory()

    def test_start(self):
        stream = self.finder.find_online_stream()
        task = self.factory.create_record_stream_video_task(stream)

        self.__run_task(task)

        path_to_video_file = utils.stream_dir.get_path_to_video_file(stream['id'])
        self.assertTrue(FileHelper.is_file_exists(path_to_video_file))

    def __run_task(self, task):
        task.start()
        time.sleep(15)
        task.stop()
