from interactor import factories


class ShowAllStreamsInfoCommand:
    def __init__(self, stream_presenter):
        self.__stream_presenter = stream_presenter
        self.__stream_gateway = factories.gateway_factory.create_stream_gateway()

    def execute(self):
        streams = self._find_all_streams()
        view_streams = self._format_streams(streams)
        return view_streams

    def _find_all_streams(self):
        return self.__stream_gateway.find_all()

    def _format_streams(self, streams):
        view_streams = []
        for stream in streams:
            view_streams.append(self.__stream_presenter.format(stream))
        return view_streams
