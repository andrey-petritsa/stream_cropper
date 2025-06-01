import utils
from interactor.task.task import Task


class RecordVideoTask(Task):
    def __init__(self, video_recorder):
        super().__init__()
        self.stream = None

        self.__video_recorder = video_recorder
        self.__stream_dir = utils.stream_dir

    def _start_task_work(self):
        self.__video_recorder.set_output(self.__get_path_to_video_file())
        self.__video_recorder.start(self.stream['link'])

    def __get_path_to_video_file(self):
        return self.__stream_dir.get_path_to_video_file(self.stream['id'])

    def _stop_task_work(self):
        self.__video_recorder.stop()

    def get_id(self):
        return f"record-video-{self.stream['link']}"


