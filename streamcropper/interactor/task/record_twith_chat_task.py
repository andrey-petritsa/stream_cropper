import threading

from interactor.task.task import Task
from twith_platform.chat.chat_reader import ChatReader
from twith_platform.chat.twith_chat_connection import TwithChatConnection
from twith_platform.config import twith_auth


class RecordTwithChatTask(Task):
    def __init__(self, stream_gateway):
        super().__init__()

        self.__stream_gateway = stream_gateway
        self.__messages = []
        self.__read_messages_thread = None
        self.__chunk_size = 2
        self.__should_stop_record = threading.Event()
        self.__is_running = False

    def _start_task_work(self):
        self.__create_twith_chat_reader(self.__stream["stream_reference"])
        self.__stream['messages'] = []

        self.__start_reading_thread()

    def _stop_task_work(self):
        self.__should_stop_record.set()
        self.__read_messages_thread.join()

    def __start_reading_thread(self):
            self.__read_messages_thread = threading.Thread(target=self.__read_chat_messages)
            self.__read_messages_thread.start()

    def __read_chat_messages(self):
        while (True):
            readed_messages = self.__twith_chat.read(self.__chunk_size)
            self.__messages.extend(readed_messages)
            self.__stream['messages'] = self.__messages
            self.__stream_gateway.save(self.__stream)
            if self.__should_stop_record.is_set():
                return 0

    def __create_twith_chat_reader(self, stream_reference):
        self.__twith_chat = ChatReader(stream_reference)
        self.__twith_chat.chat_connection = TwithChatConnection(stream_reference, twith_auth)

    def get_messages(self):
        return self.__messages

    def set_stream(self, stream):
        self.__stream = stream

    def set_chunk_size(self, chunk_size):
        self.__chunk_size = chunk_size

    def get_id(self):
        return f"record-chat-{self.__stream['stream_reference']}"