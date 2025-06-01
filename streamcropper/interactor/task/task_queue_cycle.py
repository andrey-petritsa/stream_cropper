import time

import interactor
import utils
from gui import TaskRegistryPresenter
from interactor.use_cases.end_record_stream_command import EndRecordStreamCommand
from streamcropper import AppFactory


class TaskQueueCycle:
    @classmethod
    def run(cls, watchers):
        for watcher in watchers:
            watcher.start_watch()

        time.sleep(10)

        while (True):
            for watcher in watchers:
                stream = watcher.get_stream()
                if stream['is_online']:
                    cls.__add_record_stream_task_to_queue(stream)

                if not stream['is_online']:
                    cls.__delete_record_stream_task_from_queue(stream)

                if watcher.is_stream_recorded():
                    watcher.prev_statuses = []
                    cls.__end_record_stream(stream)

            TaskRegistryPresenter.out(interactor.task_queue)
            time.sleep(15 * 1)

    @classmethod
    def __add_record_stream_task_to_queue(cls, stream):
        factory = AppFactory()
        interactor.task_queue.add_task(factory.create_record_stream_task(stream))

    @classmethod
    def __delete_record_stream_task_from_queue(cls, stream):
        task_id = f'record-stream-{stream["id"]}'
        if interactor.task_queue.is_contain(task_id):
            interactor.task_queue.delete_task(f'record-stream-{stream["id"]}')

    @classmethod
    def __end_record_stream(cls, stream):
        cmd = EndRecordStreamCommand()
        cmd.execute(stream)
        utils.logger.info(f'Stream {stream["id"]} record done')

