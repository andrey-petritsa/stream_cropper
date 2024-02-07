from mocks import SpyTask


class StubRecordStreamTaskFactory():
    def __init__(self):
        self.spy_task = SpyTask()

    def create_task(self, platform_name, stream_reference):
        self.last_created_task = self.spy_task
        self.spy_task.id = stream_reference
        return self.spy_task