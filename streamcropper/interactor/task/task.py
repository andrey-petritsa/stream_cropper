import utils

class Task():
    def __init__(self):
        self._sub_tasks = []
        self._is_running = False

    def start(self):
        if(self.is_running()):
            raise Exception(f"Task {self.get_id()} already running")

        for task in self._sub_tasks:
            task.start()

        self._start_task_work()
        self._is_running = True
        utils.logger.info(f'Task {self.get_id()} started')

    def _start_task_work(self):
        pass

    def stop(self):
        if(not self.is_running()):
            raise Exception(f"Task {self.get_id()} not running")

        for task in self._sub_tasks:
            task.stop()

        self._stop_task_work()
        self.__is_running = False
        utils.logger.info(f"Stopped {self.get_id()}")

    def _stop_task_work(self):
        pass

    def is_running(self):
        return self._is_running

    def get_id(self):
        return "not-implemented"