from interactor.use_cases import StartStreamSnipingCommandByAllStreams


class TestableStartStreamSnipingCommandByAllStreams(StartStreamSnipingCommandByAllStreams):
    def __init__(self, watch_streamers):
        super().__init__(watch_streamers)
        self.interacted_watchers = 0
        self.created_watchers = []

    def _create_watcher(self, stream):
        watcher = super()._create_watcher(stream)
        self.created_watchers.append(watcher)
        return watcher