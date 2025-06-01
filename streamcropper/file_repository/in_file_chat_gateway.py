import json
import os.path

import utils
from test_helpers.file_helper import FileHelper


class InFileChatGateway:
    def append_messages(self, stream_id, messages):
        chat_file_path = utils.stream_dir.get_path_to_chat_file(stream_id)

        if not FileHelper.is_file_exists(chat_file_path):
            f = self.__create_empty_file(chat_file_path)
        else:
            f = open(chat_file_path, 'a', encoding='utf-8')

        for msg in messages:
            str_msg = json.dumps(msg, ensure_ascii=False)
            f.write(str_msg+'\n')

        f.close()

    def __create_empty_file(self, chat_file_path):
        folder_path = os.path.dirname(chat_file_path)
        os.makedirs(folder_path, exist_ok=True)
        f = open(chat_file_path, 'w', encoding='utf-8')
        return f

    def get_messages(self, stream_id):
        chat_file_path = utils.stream_dir.get_path_to_chat_file(stream_id)
        return self.__get_messages_from_file(chat_file_path)

    def __get_messages_from_file(self, chat_file_path):
        messages = []
        with open(chat_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line == '\n':
                    continue
                msg = json.loads(line)
                messages.append(msg)

        return messages




