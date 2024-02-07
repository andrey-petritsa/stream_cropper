import json
import os
import shutil


class FileHelper:
    @staticmethod
    def read_file(path_to_file):
        f = open(path_to_file, "r")
        return f.readline()

    @staticmethod
    def read_json(path_to_file):
        f = open(path_to_file, "r")
        jsonString = f.readline()
        return json.loads(jsonString)

    @staticmethod
    def maybe_remove_file(path_to_file):
        if(os.path.isfile((path_to_file))):
            os.remove((path_to_file))

    @staticmethod
    def maybe_remove_dir(path_to_dir):
        if(os.path.isdir(path_to_dir)):
            shutil.rmtree(path_to_dir)

    @staticmethod
    def maybe_clean_dir(path_to_dir):
        if(os.path.isdir(path_to_dir)):
            for filename in os.listdir(path_to_dir):
                file_path = os.path.join(path_to_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

    @staticmethod
    def is_file_exists(path_to_file):
        return os.path.isfile(path_to_file)

    @staticmethod
    def is_dir_exists(path_to_folder):
        return os.path.isdir(path_to_folder)