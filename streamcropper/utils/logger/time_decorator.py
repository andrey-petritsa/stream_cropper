from datetime import datetime


class TimeDecorator:
    def __init__(self, logger):
        self.__logger = logger

    def info(self, message):
        self.__logger.info(self.__get_message_with_time(message))

    def error(self, message):
        self.__logger.error(self.__get_message_with_time(message))

    def __get_message_with_time(self, message):
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        message_with_time = f'{time} {message}'
        return message_with_time