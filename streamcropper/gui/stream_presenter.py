import copy

from gui.moment_presenter import MomentPresenter
from gui.moment_sorter import MomentSorter


class StreamPresenter():
    def __init__(self):
        self.__moment_presenter = MomentPresenter()
        self.__moment_sorter = MomentSorter()

        self.__sort_moment_mode = False

    def format(self, stream):
        if self.__sort_moment_mode:
            stream = self.__moment_sorter.sort_by_weights_ask(stream)

        return self.__format_stream(stream)

    def __format_stream(self, stream):
        stream_copy = copy.copy(stream)

        stream_copy['started_at'] = str(stream_copy['started_at'])
        stream_copy['messages'] = self.__format_messages(stream)

        if "moments" in stream_copy:
            stream_copy['moments'] = self.__moment_presenter.format_moments(stream)


        return stream_copy

    def set_sort_moment_mode(self):
        self.__sort_moment_mode = True

    def __format_messages(self, stream):
        view_messages = []

        for message in stream['messages']:
            view_message = copy.copy(message)
            view_message = view_message.__dict__
            view_message['datetime'] = str(view_message['datetime'])
            view_messages.append(view_message)

        return view_messages