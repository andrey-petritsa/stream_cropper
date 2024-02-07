from component.stream_analyzer.help.stream_builder import StreamBuilder
from stream_analyzer.moment_finder import MomentFinder


class FindMomentsFromChatProviderCommand:
    def __init__(self, chatProvider):
        self.__chatProvider = chatProvider
        self.__stream_builder = StreamBuilder()

    def execute(self, streamId, radius):
        stream = self.__stream_builder.build_anon_stream()
        stream['messages'] = self.__chatProvider.get_messages(streamId)
        finder = MomentFinder()
        moments = finder.find(stream, radius)
        return moments