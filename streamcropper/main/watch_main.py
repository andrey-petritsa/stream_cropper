import utils
from interactor.stream_watcher.stream_watcher import StreamWatcher
from interactor.task.task_queue_cycle import TaskQueueCycle
from utils import StdoutLogger
from utils.logger.composite_logger import CompositeLogger
from utils.logger.file_logger import FileLogger
from utils.logger.time_decorator import TimeDecorator


class WatchMain():
    def run(self):
        watchers = self.__create_stream_watchers()
        TaskQueueCycle.run(watchers)

    def __create_stream_watchers(self):
        links = [
            "https://www.twitch.tv/welovegames",
            "https://www.twitch.tv/lenagol0vach",
            "https://www.twitch.tv/rostislav_999",
            "https://www.twitch.tv/bigrussianmum",
            "https://www.twitch.tv/juice",
            "https://www.twitch.tv/ramzes"
        ]
        watchers = []

        for link in links:
            watchers.append(StreamWatcher(link))

        return watchers



logger = CompositeLogger()
logger.add_logger(TimeDecorator(FileLogger('output/log.txt')))
logger.add_logger(TimeDecorator(StdoutLogger()))
utils.logger = logger

main = WatchMain()
main.run()



