import time
import unittest

import utils
from file_repository.stream_dir import StreamDir
from integrational import test_stream_dir
from refactor.fake_id_generator import FakeIdGenerator
from test_helpers import TwithStreamFinder
from test_helpers.file_helper import FileHelper
from test_helpers.video.video_validator import VideoValidator


class TestTwithWatcher(unittest.TestCase):
    def setUp(self):
        utils.stream_dir = StreamDir(test_stream_dir)
        utils.id_generator = FakeIdGenerator()
        utils.id_generator.default_id = 'abc'
        self.registry = RecorderRegistry()
        self.video_validator = VideoValidator()
        factories.stream_watcher_factory = TestableStreamWatcherFactory()
        factories.record_stream_task_factory = TwithRecordStreamTaskFactory()
        self.factory = factories.stream_watcher_factory

    def record_some_time(self, watcher, seconds):
        finder = TwithStreamFinder()
        online_stream = finder.find_one_online_stream()
        watcher.set_stream_reference(online_stream['stream_reference'])
        watcher.__get_current_stream_event()
        time.sleep(seconds)
        last_recorder = self.registry.get_last()
        last_recorder.stop()


    def test_after_emitting_recorder_has_task(self):
        watcher = self.factory.create_stream_watcher(self.registry)
        self.record_some_time(watcher, 20)

        last_recorder = self.registry.get_last()
        self.assertEqual('abc', last_recorder.get_id())

    def test_recorder_record_video(self):
        watcher = self.factory.create_stream_watcher(self.registry)
        self.record_some_time(watcher, 20)

        last_recorded_video_path = utils.stream_dir.get_path_to_video_file(watcher.last_stream)
        self.assertEqual([], self.video_validator.validate(last_recorded_video_path))

    def test_recorder_record_chat(self):
        watcher = self.factory.create_stream_watcher(self.registry)
        self.record_some_time(watcher, 20)

        stream_meta = FileHelper.read_json(utils.stream_dir.get_path_to_meta_file(watcher.last_stream))
        self.assertNotEqual([], stream_meta['messages'])



