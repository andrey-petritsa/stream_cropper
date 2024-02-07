class FindStreamInfoCommand():
    def __init__(self, chatProvider):
        self.chatProvider = chatProvider

    def execute(self, streamId):
        info = self.chatProvider.get_stream_info(streamId)

        return info