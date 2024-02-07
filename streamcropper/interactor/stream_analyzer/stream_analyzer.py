from interactor.stream_analyzer.commands.find_moments_from_chat_provider_command import FindMomentsFromChatProviderCommand
from interactor.stream_analyzer.commands.find_stream_info_command import FindStreamInfoCommand


class StreamAnalyzer():
    def __init__(self, chatProvider, weight_builder):
        self.__chatProvider = chatProvider
        self.weight_builder = weight_builder

    def analyze_stream(self, stream_id, explosion_radius):
        find_moments_command = FindMomentsFromChatProviderCommand(self.__chatProvider)
        find_info_command = FindStreamInfoCommand(self.__chatProvider)

        analyze = {
            'explosions': find_moments_command.execute(stream_id, explosion_radius),
            'info': find_info_command.execute(stream_id)
        }

        return self.weight_builder.build(analyze)
