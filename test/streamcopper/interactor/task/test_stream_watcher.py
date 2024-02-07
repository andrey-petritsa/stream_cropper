import unittest

import interactor
import interactor.factories as factories
from interactor.stream_watcher.stream_watcher import StreamWatcher
from mocks.interactor.stub_stream_task_factory import StubRecordStreamTaskFactory
from mocks.platform.fake_platform import FakePlatform


class TestStreamWatcher(unittest.TestCase):
    def setUp(self):
        interactor.task_registry.clean()
        factories.record_stream_task_factory = StubRecordStreamTaskFactory()
        self.spy_task = factories.record_stream_task_factory.spy_task
        platform_name = "local"
        self.stream_watcher = StreamWatcher(platform_name, "orkpod")
        self.stream_watcher.platform = FakePlatform()

    def tearDown(self):
        pass

    def test_watcher_add_task_to_registry(self):
        self.stream_watcher.start_or_stop_record_task()

        self.assertEqual(1, len(interactor.task_registry))
        self.assertEqual(["start"], self.spy_task.called_methods)

    def test_watcher_delete_task_from_registry(self):
        self.stream_watcher.platform.set_schedule(["on", "off"])

        self.stream_watcher.start_or_stop_record_task()
        self.stream_watcher.start_or_stop_record_task()

        self.assertEqual(0, len(interactor.task_registry))
        self.assertEqual(["start", "stop"], self.spy_task.called_methods)

    def test_watcher_do_nothing(self):
        self.stream_watcher.platform.set_schedule(["off"])

        self.stream_watcher.start_or_stop_record_task()
        self.stream_watcher.start_or_stop_record_task()
        self.stream_watcher.start_or_stop_record_task()
        self.stream_watcher.start_or_stop_record_task()

        self.assertEqual(0, len(interactor.task_registry))
        self.assertEqual([], self.spy_task.called_methods)
