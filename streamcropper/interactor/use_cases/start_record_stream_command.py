import interactor
import interactor.factories as factories


class StartRecordStreamCommand():
    def execute(self, stream_reference, platform_name):
        task = factories.record_stream_task_factory.create_task(platform_name, stream_reference)
        task.start()
        interactor.task_registry.add_task(task, task.get_id())
