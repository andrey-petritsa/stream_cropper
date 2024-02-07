import json
import os
from datetime import datetime

import utils
from file_repository.in_file_stream_saver import InFileStreamSaver
from file_repository.json_stream_unserializer import JsonStreamUnserializer
from interactor import Moment
from test_helpers.file_helper import FileHelper


class InFileStreamGateway:
    def __init__(self):
        self.__in_file_stream_saver = InFileStreamSaver(utils.stream_dir)
        self.__json_stream_unserializer = JsonStreamUnserializer()
        self.__stream_dir = utils.stream_dir
        self.__root_dir = self.__stream_dir.get_root_dir()

    def save(self, stream):
        self.__in_file_stream_saver.save(stream)

    def find_by_id(self, stream_id):
        path_to_stream_file = self.__find_path_to_stream_file(stream_id)
        json_stream_string = FileHelper.read_file(path_to_stream_file)
        stream = json.loads(json_stream_string)

        return self.__json_stream_unserializer.unserialize(stream)

    def find_all(self):
        stream_files = self.__open_stream_files()
        streams = self.__unserialize_stream_files(stream_files)

        return streams

    def __open_stream_files(self):
        sub_folders = self.__find_all_subfolder_streams()
        stream_file_pathes = []
        for folder in sub_folders:
            stream_file_pathes.append(self.__get_path_of_stream_file(folder))
        stream_files = []
        for path in stream_file_pathes:
            stream_files.append(open(path, 'r'))
        return stream_files

    def __find_all_subfolder_streams(self):
        sub_directories_names = next(os.walk(self.__root_dir))[1]
        return sub_directories_names

    def __unserialize_stream_files(self, stream_files):
        streams = []
        for file in stream_files:
            json_stream = file.readline()
            stream = json.loads(json_stream)
            unserialized_stream = self.__json_stream_unserializer.unserialize(stream)
            streams.append(unserialized_stream)
        return streams

    def __unserialize_object_fields(self, stream):
        stream['started_at'] = datetime.fromtimestamp(stream['started_at'])
        object_moments = []
        for moment in stream['moments']:
            messages = moment['_Moment__messages']
            object_moments.append(Moment(messages))
        stream['moments'] = object_moments

    def __find_path_to_stream_file(self, stream_id):
        subfolders = self.__find_all_subfolder_streams()
        for folder in subfolders:
            if stream_id in folder:
                stream_folder = folder
                return self.__get_path_of_stream_file(stream_folder)
        raise Exception(f'Stream file not founded {stream_id}')

    def __get_path_of_stream_file(self, stream_folder):
        return f"{self.__root_dir}/{stream_folder}/meta.json"





