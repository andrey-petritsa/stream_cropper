from interactor.task.task import Task


class MultiTask(Task):
    def __init__(self):
        self.stream = None
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_id(self):
        return f'record-stream-{self.stream["id"]}'

    def _start_task_work(self):
        for task in self.tasks:
            task.start()

    def _stop_task_work(self):
        for task in self.tasks:
            task.stop()

    def is_running(self):
        for task in self.tasks:
            if task.is_running() == True:
                return True

        return False

