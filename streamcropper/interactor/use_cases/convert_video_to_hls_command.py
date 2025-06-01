import utils
from interactor.ffmpeg import FFmpeg


class ConvertVideoToHlsCommand:
    def __init__(self):
        self.__ffmpeg = FFmpeg()
        
    def execute(self, path_to_video):
        self.__ffmpeg.convert_to_hls(path_to_video)
        utils.logger.info(f'Video {path_to_video} converted to hls')




