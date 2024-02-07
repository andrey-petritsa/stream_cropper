import unittest

from gui import TaskRegistryPresenter
from interactor import TaskRegistry
from mocks import SpyTask
from mocks.gui import SpyPrintView
from test_helpers.stream_builder import StreamBuilder


class TestTaskRegistryPresenter(unittest.TestCase):
    def setUp(self):
        self.stream_builder = StreamBuilder()
        self.spy_print_view = SpyPrintView()
        self.task_registry = TaskRegistry()
        self.presenter = TaskRegistryPresenter(self.spy_print_view)

    def test_out_empty(self):
        self.presenter.out(self.task_registry)
        self.assertEqual([], self.spy_print_view.view_model)

    def test_out_one_task(self):
        task = SpyTask()
        task.id = "aaaa-bbbb-cccc-dddd"
        task.stream = self.stream_builder.get_stream()
        self.task_registry.add_task(task, 'spy-stream-recorder')
        self.presenter.out(self.task_registry)

        expected_task = {"id": "aaaa-bbbb-cccc-dddd"}
        self.assertEqual(expected_task, self.spy_print_view.view_model[0])