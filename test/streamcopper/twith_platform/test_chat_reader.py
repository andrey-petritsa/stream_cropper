import unittest

from test_helpers.message_builder import MessageBuilder
from twith_platform.chat.chat_reader import ChatReader
from twith_platform.chat.mock.stub_twith_chat_connection import StubTwithChatConnection


class TestChatReader(unittest.TestCase):
    def setUp(self):
        self.stub_twith_chat = StubTwithChatConnection()
        stream_online_reference = 'orkpod'
        self.chat = self.create_twith_chat(stream_online_reference)


    def create_twith_chat(self, stream_reference):
        chat = ChatReader(stream_reference)
        chat.chat_connection = self.stub_twith_chat
        self.stub_twith_chat.messages = [
            MessageBuilder.build_anon_message(),
            MessageBuilder.build_anon_message(),
            MessageBuilder.build_anon_message(),
        ]

        return chat

    def test_read_1_message(self):
        messages = self.chat.read(1)
        self.assertEqual('привет мир!', messages[0].text)
        self.assertEqual(1, len(messages))

    def test_read_2_messages(self):
        messages = self.chat.read(2)
        self.assertEqual(2, len(messages))

    def test_read_3_messages_seq(self):
        messages = []
        messages.extend(self.chat.read(1))
        messages.extend(self.chat.read(2))
        self.assertEqual(3, len(messages))

    def test_when_messages_read_too_long__already_readed_messages_returns(self):
        self.chat.read_timeout_sec = 0.01
        messages = self.chat.read(100)
        self.assertEqual(3, len(messages))
