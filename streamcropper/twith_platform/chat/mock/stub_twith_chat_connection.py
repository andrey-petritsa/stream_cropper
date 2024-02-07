class StubTwithChatConnection():
    def __init__(self):
        self.messages = []
        self.__is_open = False

    def open_chat_connection(self):
        self.__is_open = True

    def is_open(self):
        return self.__is_open

    def get_one_message(self):
        return self.messages.pop(0)

    def get_message_count(self):
        return len(self.messages)