import interactor

class StopTaskByIdCommand:
    def __init(self):
        pass

    def execute(self, task_id):
        interactor.task_registry.delete_task(task_id)

