import utils
from interactor.task.task import Task


class RecordVideoTask(Task):
    def __init__(self, video_recorder):
        super().__init__()

        self.__video_recorder = video_recorder
        self.__stream_dir = utils.stream_dir

        self.__stop_observers = []

    def _start_task_work(self):
        self.__video_recorder.set_output(self.__get_path_to_video_file())
        self.__video_recorder.set_platform(self.__stream['platform'])
        self.__video_recorder.start(self.__stream['stream_reference'])

    def __get_path_to_video_file(self):
        return self.__stream_dir.get_path_to_video_file(self.__stream)

    def _stop_task_work(self):
        self.__video_recorder.stop()

        for observer in self.__stop_observers:
            observer.update(self)

    def get_id(self):
        return f"record-video-{self.__stream['stream_reference']}"

    def set_stream(self, stream):
        self.__stream = stream

    def get_stream(self):
        return self.__stream

    def add_stop_observer(self, observer):
        self.__stop_observers.append(observer)
