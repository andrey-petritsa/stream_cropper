import time
import unittest

from interactor.stream_watcher.stream_watcher import StreamWatcher


class TestStreamWatcher(unittest.TestCase):
    def setUp(self):
        pass

    def test_start_watch(self):
        watcher = StreamWatcher('https://www.twitch.tv/juice')
        watcher.start_watch()
        time.sleep(1)
        self.assertTrue(watcher.is_online())

    def test_interritate_as_end_recording(self):
        watcher = StreamWatcher('https://www.twitch.tv/juice')
        watcher.prev_statuses = ['online', 'offline', 'offline']
        self.assertTrue(watcher.is_stream_recorded())

        watcher.prev_statuses = ['online', 'online']
        self.assertFalse(watcher.is_stream_recorded())

        watcher.prev_statuses = ['offline', 'offline']
        self.assertFalse(watcher.is_stream_recorded())

