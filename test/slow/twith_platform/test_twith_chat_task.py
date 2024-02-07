import time
import unittest

from interactor.task.record_twith_chat_task import RecordTwithChatTask
from mocks.interactor.in_memory_stream_gateway import InMemoryStreamGateway
from test_helpers.twith_stream_finder import TwithStreamFinder


class TestTwithChatTask(unittest.TestCase):
    def setUp(self):
        self.finder = TwithStreamFinder()
        self.stream_gateway = InMemoryStreamGateway()
        self.stream = self.finder.find_online_stream()
        self.task = self.create_task()

    def tearDown(self):
        self.task.stop()

    def create_task(self):
        task = RecordTwithChatTask(self.stream_gateway)
        task.set_stream(self.stream)
        return task

    @unittest.skip("Тест стоит запускать только с активным чатом")
    def test_read_chat(self):
        self.task.start()
        time.sleep(10)

        stream = self.stream_gateway.find_by_id(self.stream["id"])
        readed_messages = stream['messages']
        self.assertNotEqual([], readed_messages)

