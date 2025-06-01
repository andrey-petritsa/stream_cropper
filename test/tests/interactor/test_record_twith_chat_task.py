import time
import unittest

from mocks.interactor.in_memory_chat_gateway import InMemoryChatGateway
from streamcropper import AppFactory
from test_helpers.twith_stream_finder import TwithStreamFinder


class TestRecordTwithChatTask(unittest.TestCase):
    def setUp(self):
        self.finder = TwithStreamFinder()
        self.chat_gateway = InMemoryChatGateway()
        self.stream = self.finder.find_online_stream()
        self.chat_gateway.chats[self.stream['id']] = []
        self.task = self.create_task()
        self.max_chat_read_tries = 30

    def create_task(self):
        factory = AppFactory()
        task = factory.create_record_chat_task(self.stream)
        task.chat_gateway = self.chat_gateway
        return task

    def test_read_chat(self):
        self.task.start()
        chat = self.__read_chat_until_any_message_appeared()
        self.task.stop()

        self.assertNotEqual([], chat)

    def __read_chat_until_any_message_appeared(self):
        chat_read_tries = 0
        while (True):
            chat = self.chat_gateway.chats[self.stream['id']]
            if len(chat) != 0:
                break
            if chat_read_tries >= self.max_chat_read_tries:
                break
            time.sleep(1)
        return chat

