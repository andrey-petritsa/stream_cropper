import unittest

from mocks.local_chat_provider import LocalChatProvider
from streamcropper.interactor.stream_analyzer.commands.find_stream_info_command import FindStreamInfoCommand
from test_helpers.message_builder import MessageBuilder


class FindStreamInfoCommandTest(unittest.TestCase):
    message_builder = MessageBuilder()

    def test_getInfo(self):
        chatProvider = LocalChatProvider()
        chatProvider.stream_info = {
            'first_message': 'stubMessage'
        }
        findStreamInfoCommand = FindStreamInfoCommand(chatProvider)

        info = findStreamInfoCommand.execute('111-222')

        self.assertEqual(info['first_message'], 'stubMessage')

