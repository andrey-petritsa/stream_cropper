import interactor
import interactor.factories as factories
from interactor.task.null_task import NullTask


class StreamWatcher:
    def __init__(self, platform_name, stream_reference):
        self.platform = interactor.factories.platform_factory.create_platform(platform_name)
        self.__stream_reference = stream_reference
        self.__last_started_task = NullTask()

    def start_or_stop_record_task(self):
        stream = self.platform.download_stream(self.__stream_reference)
        if stream["is_online"]:
            if not self.__is_stream_already_recording():
                self.__add_task_to_registry()

        if not stream["is_online"]:
            if self.__is_stream_already_recording():
                record_stream_task = interactor.task_registry.get_by_id(self.__last_started_task.get_id())
                record_stream_task.stop()
                interactor.task_registry.delete_task(self.__last_started_task.get_id())

    def __is_stream_already_recording(self):
        return interactor.task_registry.is_contain(self.__last_started_task.get_id())

    def __add_task_to_registry(self):
        task = factories.record_stream_task_factory.create_task('twith', self.__stream_reference)
        interactor.task_registry.add_task(task, task.get_id())
        task.start()
        self.__last_started_task = task


