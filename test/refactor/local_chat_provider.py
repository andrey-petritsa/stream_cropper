class LocalChatProvider:
    stream_info = None
    messages = []

    def get_messages(self, streamId):
        return self.messages

    def get_stream_info(self, stream_id):
        return self.stream_info