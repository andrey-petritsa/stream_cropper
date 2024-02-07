
import interactor.factories as factories
from interactor.stream_analyzer.message_group_strategy.message_spam_strategy import MessageSpamStrategy
from interactor.stream_analyzer.moment_finder import MomentFinder


class ShowStreamCommand():
    def __init__(self, stream_presenter):
        self.__stream_presenter = stream_presenter
        self.__stream_gateway = factories.gateway_factory.create_stream_gateway()
        self.__moment_finder = self._create_moment_finder()

    def execute(self, stream_id, moment_radius):
        stream = self.__stream_gateway.find_by_id(stream_id)
        stream['moments'] = self.__moment_finder.find(stream, moment_radius)

        self.__stream_presenter.set_sort_moment_mode()
        view_stream = self.__stream_presenter.format(stream)

        return view_stream

    def _create_moment_finder(self):
        return MomentFinder(MessageSpamStrategy())