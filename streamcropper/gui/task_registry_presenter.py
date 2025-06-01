class TaskRegistryPresenter:
    @classmethod
    def out(cls, task_queue):
        view_tasks = []

        if len(task_queue) > 0:
            for task in task_queue.get_tasks():
                view_tasks.append(f"Task in progress: {task.get_id()} ")

            for view_task in view_tasks:
                print(view_task)

        else:
            print('No Tasks in Queue')
