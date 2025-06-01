import re

from unidecode import unidecode


class StreamIdGenerator:
    def generate(self, stream):
        valid_stream_name = self.__sanitize_stream_name(stream['name'])
        return stream['streamer']['name'] + '_' + valid_stream_name

    def __sanitize_stream_name(self, name):
        name = unidecode(name)
        name = name.lower()
        name = re.sub(r"[’‘ʼ'`′]", '', name)
        name = re.sub(r'[\\/:"*?<>|! ]+', '_', name)
        name = re.sub(r'_+', '_', name)
        return name.strip('_')
