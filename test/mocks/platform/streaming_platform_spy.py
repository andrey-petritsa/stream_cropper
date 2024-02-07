class StreamingPlatformSpy:
    last_called_funs = []
    streams = []

    def show_streams(self):
        return self.streams

    def turn_off_all_streams(self):
        for stream in self.streams:
            stream['status'] = 'offline'

    def turn_on_all_streams(self):
        for stream in self.streams:
            stream['status'] = 'online'