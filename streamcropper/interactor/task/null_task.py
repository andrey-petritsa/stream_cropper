class NullTask():
    def is_running(self):
        return False

    def start(self):
        raise Exception("Null task cannot be run")

    def stop(self):
        raise Exception("Null task cannot be stopped")

    def get_id(self):
        return "null-task"