import unittest

import interactor
from interactor.use_cases.stop_task_by_id_command import StopTaskByIdCommand
from mocks.interactor.stub_task import StubTask


class TestStopTaskByIdCommand(unittest.TestCase):
    def setUp(self):
        self.command = StopTaskByIdCommand()

    def tearDown(self):
        pass

    def test_execute(self):
        interactor.task_registry.add_task(StubTask(), 'stub-task')
        self.command.execute('stub-task')
        self.assertEqual(0, len(interactor.task_registry))
