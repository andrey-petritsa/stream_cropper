import subprocess


class Vlc:
    @staticmethod
    def play_video(path_to_video):
        process = subprocess.Popen(f'vlc {path_to_video}', shell=True)