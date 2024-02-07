import sys
print(sys.path)

import signal
import threading
import time

import interactor
import utils
from interactor.stream_watcher.stream_watcher import StreamWatcher
from utils import StdoutLogger
from utils.logger.composite_logger import CompositeLogger
from utils.logger.file_logger import FileLogger
from utils.logger.time_decorator import TimeDecorator


class WatchMain():
    def __init__(self):
        self.__is_watchers_stopped = False
        self.__watchers_threads = self.__create_watcher_threads()

    def on_sigterm(self, signal, frame):
        utils.logger.info("Stopping all tasks...")
        self.__is_watchers_stopped = True
        interactor.task_registry.clean()

    def __create_watcher_threads(self):
        threads = []
        watchers = self.__create_stream_watchers()

        for watcher in watchers:
            threads.append(threading.Thread(target=self.__forever_run_watcher, args=(watcher,)))

        return threads

    def __create_stream_watchers(self):
        streamers = [
            "welovegames",
            "lenagol0vach",
            "rostislav_999",
            "bigrussianmum",
            "juice",
        ]
        watchers = []

        for streamer in streamers:
            watchers.append(StreamWatcher('twith', streamer))

        return watchers


    def __forever_run_watcher(self, watcher):
        while(True):
            watcher.start_or_stop_record_task()
            time.sleep(10)
            if self.__is_watchers_stopped:
                return

    def run(self):
        utils.logger.info("wath-main-running")

        for thread in self.__watchers_threads:
            thread.start()

        for thread in self.__watchers_threads:
            thread.join()

logger = CompositeLogger()
logger.add_logger(TimeDecorator(FileLogger('output/log.txt')))
logger.add_logger(TimeDecorator(StdoutLogger()))
utils.logger = logger

main = WatchMain()
signal.signal(signal.SIGTERM, main.on_sigterm)
signal.signal(signal.SIGINT, main.on_sigterm)
main.run()
utils.logger.info("Watch-main finish work")


