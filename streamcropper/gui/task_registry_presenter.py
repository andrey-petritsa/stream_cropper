class TaskRegistryPresenter():
    def __init__(self, print_view):
        self.__print_view = print_view

    def out(self, task_registry):
        view_tasks = []

        if len(task_registry) > 0:
            for task in task_registry.get_tasks():
                view_tasks.append({'id': task.get_id()})

        self.__print_view.view(view_tasks)
