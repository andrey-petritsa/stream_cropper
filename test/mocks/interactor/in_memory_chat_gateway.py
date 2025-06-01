class InMemoryChatGateway:
    def __init__(self):
        self.chats = {}

    def append_messages(self, stream_id, messages):
        if stream_id not in self.chats.keys():
            self.chats[stream_id] = []

        self.chats[stream_id].extend(messages)