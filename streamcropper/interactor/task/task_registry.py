class TaskRegistry():
    def __init__(self):
        self.__tasks = {}

    def add_task(self, task, id):
        if self.is_contain(id):
            raise Exception(f'Task {id} already exists')

        self.__tasks[id] = task

    def delete_task(self, id):
        if not self.is_contain(id):
            raise Exception(f'Task with id {id} not exists')

        self.__tasks.pop(id)

    def get_by_id(self, id):
        return self.__tasks[id]

    def get_all(self):
        return self.__tasks

    def get_tasks(self):
        tasks = []
        for key in self.__tasks:
            tasks.append(self.__tasks[key])

        return tasks

    def get_one_task(self):
        return self.get_tasks()[0]

    def is_contain(self, id):
        return id in self.__tasks

    def clean(self):
        for task_key in self.__tasks:
            self.__tasks[task_key].stop()

        self.__tasks = {}

    def __len__(self):
        return len(self.__tasks)
