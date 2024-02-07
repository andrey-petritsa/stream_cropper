import datetime

from interactor import Message, User


class MessageBuilder:
    def create_messages(self, *messageTimeStrings):
        messages = []
        for messageTimeString in messageTimeStrings:
            messages.append(self.create_message(messageTimeString))
        return messages

    def create_message_written_at_iso(self, iso_date):
        return datetime.datetime.fromisoformat('2011-11-04T12:05:23')

    def create_message(self, cuteTimeString='0:0:15', message='привет!'):
        dateTime = self.__from_cute_time_string_to_datetime(cuteTimeString)
        return Message(dateTime, message, User('anon', 'аноним'))

    def create_message_written_at(self, datetime):
        return Message(datetime, 'привет!', User('anon', 'аноним'))

    @staticmethod
    def build_anon_message():
        return Message(datetime.datetime(1996, 6, 25), 'привет мир!', User('anon', 'аноним'))

    def from_cute_time_string_to_string_date(self, cuteTimeString):
        timeParts = cuteTimeString.split(':')
        time = {'hour': int(timeParts[0]), 'minute': int(timeParts[1]), 'second': int(timeParts[2])}
        return self.__create_date(time)

    def __from_cute_time_string_to_datetime(self, cuteTimeString):
        timeParts = cuteTimeString.split(':')
        time = {'hour': int(timeParts[0]), 'minute': int(timeParts[1]), 'second': int(timeParts[2])}
        return datetime.datetime(1996, 6, 25, time['hour'], time['minute'], time['second'])

    def __create_date(self, time):
        dateTime = datetime.datetime(1996, 6, 25, time['hour'], time['minute'], time['second'])
        return dateTime.strftime("%m/%d/%Y, %H:%M:%S")

    def to_cute_time_string(self, dateTime):
        return '0:0:0'