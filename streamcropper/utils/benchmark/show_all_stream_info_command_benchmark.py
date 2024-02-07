from interactor.use_cases.show_all_streams_info_command import ShowAllStreamsInfoCommand
from utils.benchmark.benchmark import Benchmark


class ShowAllStreamInfoCommandBenchmark(ShowAllStreamsInfoCommand):
    def __init__(self, stream_presenter):
        super().__init__(stream_presenter)
        self.__benchmark = Benchmark()

    def execute(self):
        view_streams = self.__benchmark.run(super().execute, 'ShowAllStreamsInfoCommand::execute')
        return view_streams

    def _find_all_streams(self):
        streams = self.__benchmark.run(super()._find_all_streams, 'ShowAllStreamsInfoCommand::findAllStreams')
        return streams

    def _format_streams(self, streams):
        self.__streams = streams

        streams = self.__benchmark.run(self.__format_streams_cb, 'ShowAllStreamsInfoCommand::format_streams')
        return streams

    def __format_streams_cb(self):
        return super()._format_streams(self.__streams)
