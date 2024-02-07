import unittest

from test_helpers.video.video_validator import VideoValidator


class TestVideoValidator(unittest.TestCase):
    def test_no_errors(self):
        validator = VideoValidator()
        video_path = 'resources/good.ts'
        errors = validator.validate(video_path)

        self.assertEqual([], errors)

    def test_has_errors(self):
        validator = VideoValidator()
        video_path = 'resources/bad.ts'
        errors = validator.validate(video_path)

        expected = 'Application provided invalid, non monotonically increasing dts to muxer in stream 0: 272426 >= 457\n'
        self.assertTrue(expected in errors[0])
