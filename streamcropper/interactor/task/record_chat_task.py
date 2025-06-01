import threading

from interactor.task.task import Task


class RecordChatTask(Task):
    def __init__(self):
        super().__init__()
        self.stream = None
        self.chat_gateway = None
        self.chat_reader = None

        self.__read_messages_thread = None
        self.__chunk_size = 2
        self.__should_stop_record = threading.Event()
        self.__is_running = False

    def _start_task_work(self):
        self.__read_messages_thread = threading.Thread(target=self.__read_chat_messages)
        self.__read_messages_thread.start()

    def _stop_task_work(self):
        self.__should_stop_record.set()
        self.__read_messages_thread.join()

    def __read_chat_messages(self):
        while (True):
            readed_messages = self.chat_reader.read(self.__chunk_size)
            self.chat_gateway.append_messages(self.stream['id'], readed_messages)
            if self.__should_stop_record.is_set():
                return 0

    def set_chunk_size(self, chunk_size):
        self.__chunk_size = chunk_size

    def get_id(self):
        return f"record-chat-{self.stream['link']}"