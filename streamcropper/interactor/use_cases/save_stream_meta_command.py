class SaveStreamMetaCommand:
    def __init__(self):
        self.stream_gateway = None
        self.platform = None

    def execute(self, stream_reference):
        stream = self.platform.download_stream(stream_reference)
        self.stream_gateway.save(stream)