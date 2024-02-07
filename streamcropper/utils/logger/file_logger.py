class FileLogger:
    def __init__(self, path_to_file):
        self.__path_to_file = path_to_file

    def info(self, message):
        f = open(self.__path_to_file, 'a')
        f.write(f"INFO {message}\n")
        f.close()

    def error(self, message):
        f = open(self.__path_to_file, 'a')
        f.write(f"ERROR {message}\n")
        f.close()