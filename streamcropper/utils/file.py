import os


class File:
    def create_dir(self, path):
        try:
            os.makedirs(path)
        except:
            pass