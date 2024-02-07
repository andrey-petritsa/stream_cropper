from datetime import datetime

from interactor import Message, User


class TwithMessage():
    def convert(self, message):
        message_body = message.split(':')[-1]
        message_user_name = message.split('!')[0].replace(":", "")
        message_user_role = 'anonym'
        message = Message(datetime.now(), message_body, User(message_user_role, message_user_name))
        return message

    def is_user_message(self, message):
        return 'PRIVMSG' in message

    def is_ping_message(self, message):
        return 'PING' in message