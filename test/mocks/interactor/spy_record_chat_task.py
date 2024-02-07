from test_helpers.message_builder import MessageBuilder


class SpyRecordChatTask():
    def __init__(self):
        self.logs = []
        self.messages = [
            MessageBuilder.build_anon_message(),
            MessageBuilder.build_anon_message(),
        ]

    def start(self):
        stream_id = self.stream['id']
        self.logs.append(f'chat record started for {stream_id}')

    def stop(self):
        stream_id = self.stream['id']
        self.logs.append(f'chat record stopped for {stream_id}')

    def set_stream(self, stream):
        self.stream = stream

    def get_messages(self):
        return self.messages