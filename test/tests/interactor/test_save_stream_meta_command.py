import unittest

from interactor.use_cases.save_stream_meta_command import SaveStreamMetaCommand
from mocks.interactor.in_memory_stream_gateway import InMemoryStreamGateway
from mocks.platform.local_platform import LocalPlatform


class TestSaveStreamMetaCommand(unittest.TestCase):
    def test_execute(self):
        stream_gateway = InMemoryStreamGateway()
        platform = LocalPlatform()

        command = SaveStreamMetaCommand()
        command.stream_gateway = stream_gateway
        command.platform = platform

        command.execute('orkpod')

        self.assertEqual(stream_gateway.stream['id'], 'orkpod')



