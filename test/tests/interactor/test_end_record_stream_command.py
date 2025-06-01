import unittest

from interactor.use_cases.end_record_stream_command import EndRecordStreamCommand


class TestableEndRecordStreamCommand(EndRecordStreamCommand):
    def __init__(self):
        self.actions = []

    def _copy_video_to_s3(self, video_path_in, video_path_out):
        self.actions.append(f'cp video {video_path_in} to s3 {video_path_out}')

    def _delete_video(self, video_path_in):
        self.actions.append(f'delete video {video_path_in}')

class TestEndRecordStreamCommand(unittest.TestCase):
    def test_execute(self):
        cmd = TestableEndRecordStreamCommand()
        stream = {'id': 'juice'}
        cmd.execute(stream)

        self.assertEqual('cp video ./output/juice/video.ts to s3 juice/video.ts', cmd.actions[0])
        self.assertEqual('delete video ./output/juice/video.ts', cmd.actions[1])
