class SpyLogger():
    info_messages = []

    def info(self, message):
        self.info_messages.append(message)
