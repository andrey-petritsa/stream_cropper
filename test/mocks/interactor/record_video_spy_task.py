from test_helpers.stream_builder import StreamBuilder


class RecordVideoSpyTask():
    def __init__(self):
        builder = StreamBuilder()
        builder.build_stream()
        self.stream = builder.get_stream()

    def get_stream(self):
        return self.stream