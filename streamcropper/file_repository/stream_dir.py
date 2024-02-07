class StreamDir:
    def __init__(self, root_dir):
        self.__root_dir = root_dir

    def get_stream_dir(self, stream):
        parts = [stream['id']]
        stream_dir = "_".join(parts)
        stream_dir = stream_dir.replace(':', '.') # Линукс не поддерживает : в именах директорий
        return f"{self.__root_dir}/{stream_dir}"

    def get_path_to_meta_file(self, stream):
        return f"{self.get_stream_dir(stream)}/meta.json"

    def get_path_to_video_file(self, stream):
        return f"{self.get_stream_dir(stream)}/video.ts"

    def get_path_to_log_file(self, stream):
        return f"{self.get_stream_dir(stream)}/log.log"

    def get_path_to_chat_file(self, stream):
        return f"{self.get_stream_dir(stream)}/chat.txt"

    def get_root_dir(self):
        return self.__root_dir

