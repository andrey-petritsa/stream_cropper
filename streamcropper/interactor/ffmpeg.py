import os
import subprocess


class FFmpeg():
    def show_video_errors(self, video_path):
        cmd = f'ffmpeg -v error -i {video_path} -f null -'
        process = subprocess.run(cmd, shell=True, capture_output=True)
        string_error = process.stderr.decode('utf-8')
        if len(string_error) == 0:
            return []
        return [string_error]

    def convert_to_hls(self, path_to_file):
        path_to_out_folder = os.path.dirname(path_to_file) + '/hls'
        file_name_without_ext = os.path.basename(path_to_file).split('.')[0]

        os.makedirs(path_to_out_folder)
        cmd = f"ffmpeg -i {path_to_file} -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls {path_to_out_folder}/{file_name_without_ext}.m3u8 -hide_banner -loglevel error"

        subprocess.check_output(cmd, shell=True)