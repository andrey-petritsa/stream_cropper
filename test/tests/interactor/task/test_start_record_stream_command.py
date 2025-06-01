import unittest

import interactor.factories as factories

import interactor
from interactor import TaskQueue
from interactor.use_cases.start_record_stream_command import StartRecordStreamCommand
from mocks.interactor.stub_stream_task_factory import StubRecordStreamTaskFactory
from mocks.platform.local_platform import LocalPlatform
from test_helpers.stream_builder import StreamBuilder
from twith_platform.platform_factory import PlatformFactory


class TestStartRecordStreamCommand(unittest.TestCase):
    def setUp(self):
        factories.record_stream_task_factory = StubRecordStreamTaskFactory()
        interactor.platform_factory= PlatformFactory()
        interactor.task_registry = TaskQueue()
        self.local_platform = LocalPlatform()
        self.command = StartRecordStreamCommand()
        self.stream_builder = StreamBuilder()

    def tearDown(self):
        interactor.task_registry.clean()

    def test_command_call_recorder_start(self):
        self.command.execute('orkpod', 'local')
        self.added_task = interactor.task_registry.get_one_task()

        self.assertEqual('start orkpod', self.added_task.get_log())

    def test_command_add_task_to_registry(self):
        self.command.execute('orkpod', 'local')

        self.assertTrue(interactor.task_registry.is_contain('orkpod'))
