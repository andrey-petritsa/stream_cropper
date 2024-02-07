import unittest

from interactor.task.record_stream_task import RecordStreamTask
from mocks.interactor.in_memory_stream_gateway import InMemoryStreamGateway
from mocks.interactor.spy_record_chat_task import SpyRecordChatTask
from mocks.interactor.spy_record_video_task import SpyRecordVideoTask
from mocks.platform.local_platform import LocalPlatform


class TestRecordStreamTask(unittest.TestCase):
    def create_task(self):
        platform = LocalPlatform()
        stream = platform.download_stream('orkpod')

        self.spy_chat_recorder = SpyRecordChatTask()
        self.spy_chat_recorder.set_stream(stream)

        self.spy_video_recorder = SpyRecordVideoTask()
        self.spy_video_recorder.set_stream(stream)

        self.in_memory_stream_gateway = InMemoryStreamGateway()

        task = RecordStreamTask(self.in_memory_stream_gateway)
        task.add_record_chat_task(self.spy_chat_recorder)
        task.add_record_video_task(self.spy_video_recorder)
        task.set_stream(self.create_stream())
        return task

    def create_stream(self):
        return {
            "id": "AA-BB-CC-DD",
            "streamer": {
                "name": "igorghk-best"
            },
            "name": "test_stream",
            "stream_reference": 'igorghk',
        }

    def test_save_stream_into_gateway(self):
        task = self.create_task()
        task.start()
        task.stop()

        expected_stream = {
            "id": "AA-BB-CC-DD",
            "name": "test_stream",
            "streamer": {
                "name": "igorghk-best",
            },
            "stream_reference": 'igorghk',
        }
        self.assertStreamsEqual(self.in_memory_stream_gateway.stream, expected_stream)

    def test_recorders_called(self):
        task = self.create_task()
        task.start()
        task.stop()

        self.assertEqual('chat record started for orkpod', self.spy_chat_recorder.logs[0])
        self.assertEqual('video record started for orkpod', self.spy_video_recorder.logs[0])
        self.assertEqual('chat record stopped for orkpod', self.spy_chat_recorder.logs[1])
        self.assertEqual('video record stopped for orkpod', self.spy_video_recorder.logs[1])

    def assertStreamsEqual(self, first, second):
        del first['id']
        del second['id']
        self.assertEqual(first, second)
