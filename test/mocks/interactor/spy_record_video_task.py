class SpyRecordVideoTask():
    logs = []

    def start(self):
        self.stream = self.stream
        self.logs.append(f'video record started for {self.stream["stream_reference"]}')

    def stop(self):
        self.logs.append(f'video record stopped for {self.stream["stream_reference"]}')

    def set_stream(self, stream):
        self.stream = stream