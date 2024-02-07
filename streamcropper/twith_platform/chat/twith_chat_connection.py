import logging
import threading

import websocket

from twith_platform.twith_message import TwithMessage


class TwithChatConnection():
    def __init__(self, stream_name, auth):
        logging.getLogger('websockets.server').setLevel(logging.ERROR)
        logging.getLogger('websockets.protocol').setLevel(logging.ERROR)

        self.twith_message = TwithMessage()
        self.messages = []
        self.__auth = auth
        self.__stream_name = stream_name
        self.__is_opened = False

    def is_open(self):
        return self.__is_opened

    def get_one_message(self):
        return self.messages.pop(0)

    def get_message_count(self):
        return len(self.messages)

    def open_chat_connection(self):
        chat_websocket = websocket.WebSocketApp("ws://irc-ws.chat.twitch.tv", on_open=self.__on_open,
                                                on_message=self.__on_message)
        self.__listen_chat_thread = threading.Thread(target=chat_websocket.run_forever, daemon=True)
        self.__listen_chat_thread.start()

    def __on_open(self, ws):
        ws.send(f"PASS {self.__auth['token']}")
        ws.send(f"NICK {self.__auth['nick']}")
        ws.send(f"JOIN #{self.__stream_name}")

        self.__is_opened = True

    def __on_message(self, ws, raw_message):
        if(self.twith_message.is_user_message(raw_message)):
            message = self.twith_message.convert(raw_message)
            self.messages.append(message)

        if(self.twith_message.is_ping_message(raw_message)):
            pong_message = raw_message.replace('PING', 'PONG')
            ws.send(pong_message)