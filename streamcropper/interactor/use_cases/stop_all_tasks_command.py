import interactor

class StopAllTasksCommand():
    def execute(self):
        interactor.task_registry.clean()