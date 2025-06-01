import unittest

from test_helpers.video.video_validator import VideoValidator


class TestVideoValidator(unittest.TestCase):
    def test_no_errors(self):
        validator = VideoValidator()
        video_path = 'resources/streams/example_stream/video.ts'
        errors = validator.validate(video_path)

        self.assertEqual([], errors)
