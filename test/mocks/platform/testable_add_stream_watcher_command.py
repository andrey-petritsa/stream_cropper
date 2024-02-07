from interactor.use_cases.add_stream_watcher_command import AddStreamWatcherCommand


class TestableAddStreamWatcherCommand(AddStreamWatcherCommand):
    def __init__(self):
        self.watch_stream_task = None

    def _create_watch_stream_task(self, platform_name):
        return self.watch_stream_task
