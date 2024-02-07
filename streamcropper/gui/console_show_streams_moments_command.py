from gui.stream_presenter import StreamPresenter
from interactor.use_cases.show_stream_command import ShowStreamCommand


class ConsoleShowStreamsMomentsCommand():
    def __init__(self):
        self.__show_streams_command = ShowStreamCommand()
        self.__stream_presenter = StreamPresenter()

    def execute(self, moment_radius):
        streams = self.__show_streams_command.execute(moment_radius)
        view_streams = self.__stream_presenter.format(streams)

        for stream in view_streams:
            stream_string = ""
            stream_string += stream['id']+'\n'
            for moment in stream['moments']:
                stream_string += f'Вес:{moment["weight"]} Время:{moment["start"]} Смещение старт:{moment["start_delta"]} Смещение конец:{moment["end_delta"]}\n '

            print(stream_string)


