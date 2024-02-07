import datetime

from interactor import Message, User
from mocks.interactor.moment_stub import MomentStub
from test_helpers.message_builder import MessageBuilder


class StreamBuilder():
    def __init__(self, platform=None, stream_finder=None):
        self.__stream_reference = 'acrosspaper'
        self.__platform = platform
        self.__stream_finder = stream_finder
        self.__stream = None

        self.message_builder = MessageBuilder()

    def build_stream(self):
        self.__stream = {
            "id": "aaaa-bbbb-cccc-dddd",
            "messages": [self.__create_anon_message(), self.__create_anon_message()],
            "streamer": {
                "name": "acrosspaper"
            },
            "name": 'test-stream',
            "video": "/tmp/video.mkv",
            "stream_reference": self.__stream_reference,
            "platform": 'local',
            "started_at": datetime.datetime.fromisoformat('2011-11-04T12:00:00'),
        }

    def set_messages(self, *messageTimeStrings):
        messages = self.message_builder.create_messages(*messageTimeStrings)
        self.__stream['messages'] = messages

    def set_moments(self):
        self.__stream['moments'] = [
            MomentStub(4, '2011-11-04T12:01:15'),
            MomentStub(1, '2011-11-04T12:00:00'),
        ]

    def get_stream(self):
        return self.__stream

    def set_stream_reference(self, stream_reference):
        self.__stream_reference = stream_reference

    def __create_anon_message(self):
        return Message(datetime.datetime.fromisoformat('2011-11-04T12:05:23'), 'привет мир', User('moderator', 'acrosspaper'))