from interactor.ffmpeg import FFmpeg


class VideoValidator:
    def __init__(self):
        self.__ffmpeg = FFmpeg()


    def validate(self, video_path):
        return self.__ffmpeg.show_video_errors(video_path)
