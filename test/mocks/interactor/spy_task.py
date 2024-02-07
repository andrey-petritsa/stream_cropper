class SpyTask():
    def __init__(self):
        self.called_methods = []

        self.stream = None
        self.log = []
        self.id = "spy-task"
        self.is_running_flag = False

    def start(self):
        self.log.append(f'start {self.id}')
        self.is_running_flag = True
        self.called_methods.append('start')

    def stop(self):
        self.log.append(f'stop {self.id}')
        self.is_running_flag = False
        self.called_methods.append('stop')

    def is_running(self):
        return self.is_running_flag

    def get_id(self):
        return self.id

    def get_log(self):
        return " ".join(self.log)

    def __str__(self):
        return self.get_id()

