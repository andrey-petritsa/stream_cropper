import time

import utils


class ChatReader():
    def __init__(self, stream_name):
        self.read_timeout_sec = 10
        self.messages = []
        self.__stream_name = stream_name

    def read(self, message_count):
        if not self.chat_connection.is_open():
            self.chat_connection.open_chat_connection()

        self.__start = time.time()

        while(True):
            if self.chat_connection.get_message_count() >= message_count:
                return self.__read_messages_from_connection(message_count)

            self.__current = time.time()
            if self.__is_read_timeout():
                utils.logger.info(f'Chat read timeout {self.__stream_name} read only {self.chat_connection.get_message_count()}')
                return self.__read_messages_from_connection(self.chat_connection.get_message_count())

    def __read_messages_from_connection(self, amount):
        messages = []
        for _ in range(amount):
            messages.append(self.chat_connection.get_one_message())
        return messages

    def __is_read_timeout(self):
        time_diff = float(self.__current - self.__start)
        return time_diff >= self.read_timeout_sec

    def set_chat_connection(self, chat_connection):
        self.chat_connection = chat_connection
