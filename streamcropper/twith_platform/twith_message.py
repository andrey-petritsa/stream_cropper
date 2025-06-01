from datetime import datetime


class TwithMessage():
    def convert(self, message):
        message_body = message.split(':')[-1]
        message_user_name = message.split('!')[0].replace(":", "")

        return {
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'text': message_body,
            'user': {'name': message_user_name, 'role': 'anonym'}
        }

    def is_user_message(self, message):
        return 'PRIVMSG' in message

    def is_ping_message(self, message):
        return 'PING' in message