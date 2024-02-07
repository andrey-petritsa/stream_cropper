import interactor.factories as factories
from interactor.convert_video_to_hls_observer import ConvertVideoToHlsObserver
from interactor.streamlink_recorder import StreamlinkRecorder
from interactor.task.record_stream_task import RecordStreamTask
from interactor.task.record_twith_chat_task import RecordTwithChatTask
from interactor.task.record_video_task import RecordVideoTask
from twith_platform.config import twith_auth


class RecordStreamTaskFactory():
    def __init__(self):
        self.__twith_auth = twith_auth

    def create_task(self, platform_name, stream_reference):
        if 'twith' in platform_name:
            platform = factories.platform_factory.create_platform(platform_name)
            stream = platform.download_stream(stream_reference)
            task = RecordStreamTask(factories.gateway_factory.create_stream_gateway())
            task.add_record_video_task(self.__create_video_task(stream))
            task.add_record_chat_task(self.__create_chat_task(stream))
            task.set_stream(stream)
            return task

        raise Exception('This platform not supported')

    def __create_video_task(self, stream):
        task = RecordVideoTask(StreamlinkRecorder())
        task.set_stream(stream)
        task.add_stop_observer(ConvertVideoToHlsObserver())
        return task

    def __create_chat_task(self, stream):
        chat_task = RecordTwithChatTask(factories.gateway_factory.create_stream_gateway())
        chat_task.set_stream(stream)
        return chat_task