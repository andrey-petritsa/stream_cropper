import utils
from file_repository.in_file_chat_gateway import InFileChatGateway
from file_repository.stream_dir import StreamDir
from resources import test_stream_dir
from test_helpers.file_helper import FileHelper


class TestInFileChatGateway:
    def setUp(self):
        utils.stream_dir = StreamDir(test_stream_dir)

    def tearDown(self):
        FileHelper.maybe_remove_dir(utils.stream_dir.get_stream_dir('orkpod'))

    def test_append_messages(self):
        gateway = InFileChatGateway()
        gateway.append_messages('orkpod', ['привет'])

        msgs = gateway.get_messages('orkpod')
        assert msgs[0] == 'привет'