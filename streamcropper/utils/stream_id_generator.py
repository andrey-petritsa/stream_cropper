class StreamIdGenerator:
    def generate(self, stream):
        return "-".join(self.__get_hash_parts(stream))

    def __get_hash_parts(self, stream):
        date_part = stream['started_at'].strftime("%Y-%m-%d.%H-%M-%S")
        return [stream['streamer']['name'], date_part]
