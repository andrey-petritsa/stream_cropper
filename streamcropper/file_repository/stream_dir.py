class StreamDir:
    def __init__(self, root_dir):
        self.__root_dir = root_dir

    def get_stream_dir(self, stream_id):
        stream_dir = stream_id
        stream_dir = stream_dir.replace(':', '.')
        return f"{self.__root_dir}/{stream_dir}"

    def get_path_to_meta_file(self, stream_id):
        return f"{self.get_stream_dir(stream_id)}/meta.json"

    def get_path_to_video_file(self, stream_id):
        return f"{self.get_stream_dir(stream_id)}/video.ts"

    def get_path_to_log_file(self, stream_id):
        return f"{self.get_stream_dir(stream_id)}/log.log"

    def get_path_to_chat_file(self, stream_id):
        return f"{self.get_stream_dir(stream_id)}/chat.txt"

    def get_root_dir(self):
        return self.__root_dir

