import time
import unittest

import utils
from file_repository.stream_dir import StreamDir
from interactor.record_stream_task_factory import RecordStreamTaskFactory
from slow import test_stream_dir
from test_helpers.file_helper import FileHelper
from test_helpers.twith_stream_finder import TwithStreamFinder
from utils import StdoutLogger


class TestRecordStreamTask(unittest.TestCase):
    def setUp(self):
        utils.stream_dir = StreamDir(test_stream_dir)
        FileHelper.maybe_clean_dir(test_stream_dir)
        utils.logger = StdoutLogger()

        self.finder = TwithStreamFinder()
        self.factory = RecordStreamTaskFactory()

    def test_start(self):
        stream_reference = self.finder.find_online_stream()['stream_reference']
        self.task = self.factory.create_task('twith', stream_reference)
        stream = self.task.get_stream()

        self.task.start()
        time.sleep(15)
        self.task.stop()

        path_to_meta_file = utils.stream_dir.get_path_to_meta_file(stream)
        self.assertTrue(FileHelper.is_file_exists(path_to_meta_file))
