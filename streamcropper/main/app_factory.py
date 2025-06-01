from file_repository.in_file_chat_gateway import InFileChatGateway
from file_repository.in_file_stream_gateway import InFileStreamGateway
from interactor.streamlink_recorder import StreamlinkRecorder
from interactor.task.multi_task import MultiTask
from interactor.task.record_chat_task import RecordChatTask
from interactor.task.record_video_task import RecordVideoTask
from interactor.use_cases.convert_video_to_hls_command import ConvertVideoToHlsCommand
from interactor.use_cases.save_stream_meta_command import SaveStreamMetaCommand
from twith_platform import Twith
from twith_platform.chat.chat_reader import ChatReader
from twith_platform.chat.twith_chat_connection import TwithChatConnection
from twith_platform.config import twith_auth
from twith_platform.twith.streamlink_check_online_strategy import StreamlinkCheckOnlineStrategy


class AppFactory:
    def create_record_stream_video_task(self, stream):
        task = RecordVideoTask(StreamlinkRecorder())
        task.stream = stream
        return task

    def create_convert_video_to_hls_command(self):
        return ConvertVideoToHlsCommand()

    def create_record_chat_task(self, stream):
        task = RecordChatTask()
        task.stream = stream
        task.chat_gateway = InFileChatGateway()
        task.chat_reader = self.__create_twith_chat_reader(stream)
        return task

    def create_save_stream_meta_command(self):
        command = SaveStreamMetaCommand()
        command.stream_gateway = InFileStreamGateway()
        command.platform = self.__create_twith_platform()

        return command

    def create_record_stream_task(self, stream):
        task = MultiTask()
        task.stream = stream
        record_video_task = self.create_record_stream_video_task(stream)
        record_chat_task = self.create_record_chat_task(stream)
        task.add_task(record_video_task)
        task.add_task(record_chat_task)
        return task

    def __create_twith_chat_reader(self, stream):
        chat_reader = ChatReader(stream['link'])
        chat_reader.chat_connection = TwithChatConnection(stream['link'], twith_auth)
        return chat_reader

    def __create_twith_platform(self):
        return Twith(StreamlinkCheckOnlineStrategy())