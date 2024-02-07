from interactor.task.task_registry import TaskRegistry


class SpyTaskRegistry(TaskRegistry):
    def __init__(self):
        super().__init__()
        self.last_deleted_task_id = None
        self.last_added_task_id = None

    def delete_task(self, id):
        super().delete_task(id)
        self.last_deleted_task_id = id
