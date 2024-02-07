class InMemoryStreamGateway():
    def __init__(self):
        self.stream = None
        self.find_call_count = 0
        self.is_find_all_call = False

    def save(self, stream):
        self.stream = stream

    def append_chat_message(self, message):
        pass

    def find_by_id(self, id):
        self.find_call_count += 1
        return self.stream

    def find_all(self):
        self.is_find_all_call = True

        if self.stream is None:
            return []

        return [self.stream]