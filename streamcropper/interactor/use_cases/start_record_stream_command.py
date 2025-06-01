import interactor


class StartRecordStreamCommand():
    def execute(self, stream_reference, platform_name):
        task = None
        task.start()
        interactor.task_registry.add_task(task, task.get_id())
