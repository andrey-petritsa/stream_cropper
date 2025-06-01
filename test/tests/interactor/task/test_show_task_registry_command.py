import unittest

import interactor
from interactor import TaskQueue
from interactor.use_cases.show_task_registry_command import ShowTaskRegistryCommand
from mocks.gui.spy_task_registry_presenter import SpyTaskRegistryPresenter


class TestShowTaskRegistry(unittest.TestCase):
    def test_execute(self):
        interactor.task_registry = TaskQueue()
        interactor.task_registry.add_task('important-task', '123-id')
        spy_task_registry_presenter = SpyTaskRegistryPresenter()
        command = ShowTaskRegistryCommand(spy_task_registry_presenter)
        
        command.execute()

        self.assertEqual('important-task', spy_task_registry_presenter.task_registry.get_by_id('123-id'))