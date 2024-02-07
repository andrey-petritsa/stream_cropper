import time
import unittest

from interactor.streamlink_recorder import StreamlinkRecorder
from test_helpers.file_helper import FileHelper
from test_helpers.twith_stream_finder import TwithStreamFinder


class TestStreamlinkRecorder(unittest.TestCase):
    def setUp(self):
        FileHelper.maybe_remove_file("/tmp/test-video.ts")

    def test_record(self):
        stream = TwithStreamFinder().find_online_stream()
        recorder = StreamlinkRecorder()
        recorder.set_output('/tmp/test-video.ts')
        recorder.set_platform('twitch.tv')
        recorder.start(stream['stream_reference'])
        time.sleep(10)
        recorder.stop()

        self.assertTrue(FileHelper.is_file_exists('/tmp/test-video.ts'))