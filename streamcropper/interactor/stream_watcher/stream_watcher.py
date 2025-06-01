import threading
import time

import utils
from interactor.stream_watcher.stream_reference_extractor import StreamerNameExtractor
from twith_platform.platform_factory import PlatformFactory


class StreamWatcher:
    def __init__(self, stream_link):
        self.__stream_link = stream_link
        self.prev_statuses = []

        self.stream = None

    def start_watch(self):
        thread = self.__create_check_is_online_thread()
        thread.start()

    def __create_check_is_online_thread(self):
        self.__platform = PlatformFactory.create_platform(self.__stream_link)
        self.__stream_reference = StreamerNameExtractor.get(self.__stream_link)

        thread = threading.Thread(target=self.__check_is_stream_online)
        return thread

    def __check_is_stream_online(self):
        while(True):
            utils.logger.info(f'Check stream status {self.__stream_link}')
            stream = self.__platform.download_stream(self.__stream_link)
            self.stream = stream
            if self.is_online():
                self.prev_statuses.append('online')
            if not self.is_online():
                self.prev_statuses.append('offline')
            time.sleep(30)

    def is_online(self):
        if self.stream == None:
            raise Exception('Stream should not be none')

        return self.stream['is_online']

    def get_prev_statuses(self):
        return self.prev_statuses

    def get_stream(self):
        return self.stream

    def is_stream_recorded(self):
        if 'online' in self.prev_statuses and 'offline' in self.prev_statuses:
            self.prev_statuses = []
            return True
        return False



