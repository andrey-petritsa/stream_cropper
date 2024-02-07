from pathlib import Path

from file_repository.json_stream_serializer import JsonStreamSerializer


class InFileStreamSaver():
    def __init__(self, stream_dir):
        self.__stream_dir = stream_dir
        self.__json_stream_serializer = JsonStreamSerializer()

    def save(self, stream):
        self.__write_stream_to_file(stream)

    def __write_stream_to_file(self, stream):
        path_to_stream_dir = self.__stream_dir.get_stream_dir(stream)
        self.__create_dir_if_not_exists(path_to_stream_dir)
        self.__write_json_stream_to_file(stream)

    def __write_json_stream_to_file(self, stream):
        json_stream = self.__json_stream_serializer.convert_to_json(stream)
        f = open(self.__stream_dir.get_path_to_meta_file(stream), "w")
        f.write(json_stream)
        f.close()

    def __create_dir_if_not_exists(self, dir_path):
        Path(dir_path).mkdir(parents=True, exist_ok=True)
