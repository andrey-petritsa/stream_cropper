import datetime


class LocalPlatform():
    def __init__(self):
        self.is_stream_online_flag = True
        self.last_requested_streamer = None
        self.__last_shredinger_online_status = True

    def download_stream(self, stream_link):
        orkpod = {
            "id": "orkpod",
            "name": "orkpod stream",
            "streamer": {
                "name": "orkpod",
            },
            "is_online": self.is_stream_online(stream_link),
            "stream_reference": 'orkpod',
            "started_at": datetime.datetime.now(),
            "messages": []
        }
        juice = {
            "id": "juice",
            "name": "juice stream",
            "streamer": {
                "name": "juice",
            },
            "is_online": self.is_stream_online(stream_link),
            "stream_reference": 'juice',
            "started_at": datetime.datetime.now(),
            "messages": []
        }
        offline_streamer = {
            "id": "offline_streamer",
            "name": "offline",
            "streamer": {
                "name": "juice",
            },
            "is_online": False,
            "stream_reference": 'offline_streamer',
            "started_at": datetime.datetime.now(),
            "messages": []
        }
        online_streamer = {
            "id": "online_streamer",
            "name": "online",
            "streamer": {
                "name": "juice",
            },
            "is_online": True,
            "stream_reference": 'online_streamer',
            "started_at": datetime.datetime.now(),
            "messages": []
        }


        if 'orkpod' in stream_link:
            return orkpod
        if 'juice' in stream_link:
            return juice
        if 'offline' in stream_link:
            return offline_streamer
        if 'online' in stream_link:
            return online_streamer

        raise Exception(f'Streamer {stream_link} not found')

    def download_streams(self, stream_references):
        return [
            self.download_stream(stream_references[0]),
        ]

    def is_stream_online(self, stream_name):
        self.last_requested_streamer = stream_name
        return self.is_stream_online_flag

    def turn_on_streams(self):
        self.is_stream_online_flag = True

    def turn_off_streams(self):
        self.is_stream_online_flag = False

    def get_platform_name(self):
        return "local"