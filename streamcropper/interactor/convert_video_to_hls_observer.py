import shutil

import utils
from interactor.ffmpeg import FFmpeg


class ConvertVideoToHlsObserver:
    def __init__(self):
        self.__ffmpeg = FFmpeg()
        
    def update(self, record_video_task_subject):
        self.__stream = record_video_task_subject.get_stream()

        self.__convert_stream_video_to_hls()
        utils.logger.info(f'Video {self.__path_to_stream_video } converted to hls and deployed at /var/hls/')

    def __convert_stream_video_to_hls(self):
        self.__path_to_stream_video = utils.stream_dir.get_path_to_video_file(self.__stream)
        self.__ffmpeg.convert_to_hls(self.__path_to_stream_video)
        self.__deploy_hls_folder(self.__stream)

    def __deploy_hls_folder(self, stream):
        hls_dir = utils.stream_dir.get_stream_dir(stream) + '/hls'
        shutil.move(hls_dir, f'/var/hls/{stream["id"]}')




