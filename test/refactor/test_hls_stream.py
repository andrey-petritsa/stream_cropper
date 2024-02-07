import os
import unittest

import ffmpeg_streaming
from ffmpeg_streaming import Formats


class HlsStreamTest(unittest.TestCase):
    def test_creating_m3up(self):
        video = ffmpeg_streaming.input('/var/media/music-video/original/video.mp4')
        hls = video.hls(Formats.h264())
        hls.auto_generate_representations()
        hls.output('/var/media/1-hls/hls.m3u8')

        self.assertTrue(os.path.isfile('/var/media/1-hls/hls.m3u8') )