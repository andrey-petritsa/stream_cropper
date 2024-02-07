import copy
import json


class JsonStreamSerializer():
    def convert_to_json(self, stream):
        serializable_stream = self.__serialize_stream(stream)
        return json.dumps(serializable_stream, default=lambda o: o.__dict__, ensure_ascii=False)

    def __serialize_stream(self, stream):
        stream_copy = copy.deepcopy(stream)
        return self.__serialize_stream_copy(stream_copy)

    def __serialize_stream_copy(self, stream_copy):
        for message in stream_copy['messages']:
            message.datetime = message.datetime.isoformat()
        stream_copy['started_at'] = stream_copy['started_at'].isoformat()

        return stream_copy