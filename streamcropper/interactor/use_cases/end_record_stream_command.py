import utils
from test_helpers.file_helper import FileHelper
from utils.s3_bucket import S3Bucket


class EndRecordStreamCommand():
    def execute(self, stream):
        stream_dir = utils.stream_dir
        video_path_in = stream_dir.get_path_to_video_file(stream['id'])
        video_path_out = f'{stream["id"]}/video.ts'

        self._copy_video_to_s3(video_path_in, video_path_out)
        self._delete_video(video_path_in)

    def _copy_video_to_s3(self, video_path_in, video_path_out):
        S3Bucket.upload_file(video_path_in, video_path_out)

    def _delete_video(self, video_path_in):
        FileHelper.maybe_remove_file(video_path_in)
