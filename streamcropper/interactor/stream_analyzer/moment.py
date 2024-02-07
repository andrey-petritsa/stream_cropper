class Moment():
    def __init__(self, messages):
        self.__messages = messages

    def get_weight(self):
        return len(self.__messages)

    def get_start(self):
        return self.__messages[0].datetime

    def get_end(self):
        return self.__messages[-1].datetime

    def __str__(self):
        date_times = []
        for message in self.__messages:
            date_times.append(message.datetime.strftime('%H:%M:%S'))
        return " ".join(date_times)

