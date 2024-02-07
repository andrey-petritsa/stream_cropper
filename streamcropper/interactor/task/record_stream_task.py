from interactor.task.task import Task


class RecordStreamTask(Task):
    def __init__(self, stream_gateway):
        super().__init__()
        self.__stream_gateway = stream_gateway

    def start(self):
        self.__stream_gateway.save(self.stream)
        super().start()

    def get_id(self):
        return f"record-stream-{self.stream['stream_reference']}"

    def add_record_video_task(self, task):
        self.__record_video_task = task
        self._sub_tasks.append(task)

    def add_record_chat_task(self, task):
        self.__record_chat_task = task
        self._sub_tasks.append(task)

    def get_stream(self):
        return self.stream

    def set_stream(self, stream):
        self.stream = stream
