from recorder.provider.youtube_chat_provider import YoutubeChatProvider


class TestableYoutubeChatProvider(YoutubeChatProvider):
    messages = []

    def _get_messages_from_chat_provider(self, streamId):
        return self.messages