import copy
from datetime import datetime

from interactor.stream_analyzer.data.message import Message


class JsonStreamUnserializer():
    def unserialize(self, stream):
        unserialized_stream = copy.copy(stream)

        unserialized_stream['started_at'] = datetime.fromisoformat(stream['started_at'])

        messages = []
        for message in unserialized_stream['messages']:
            message_datetime = datetime.fromisoformat(message['datetime'])
            messages.append(Message(message_datetime, message['text'], message['user']))

        unserialized_stream['messages'] = messages

        return unserialized_stream