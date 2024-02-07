from datetime import datetime


class FakePlatform:
    def __init__(self):
        self.i = 0
        self.schedule = ["on", "off", "on", "off"]

        self.stream = {
            "id": "bigrussianmum-stub-name-2011-11-04",
            "name": "stub-name",
            "streamer": {
                "name": "bigrussianmum",
            },
            "is_online": True,
            "stream_reference": 'bigrussianmum',
            "started_at": datetime.fromisoformat('2011-11-04T12:05:23')
        }

    def set_schedule(self, schedule):
        self.schedule = schedule

    def download_stream(self, stream_reference):
        if self.i > len(self.schedule) - 1:
            return self.stream

        if self.schedule[self.i] == "on":
            self.stream["is_online"] = True
        else:
            self.stream["is_online"] = False

        self.i = self.i + 1

        return self.stream

    def get_platform_name(self):
        return "fake_platform"

