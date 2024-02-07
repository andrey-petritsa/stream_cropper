class PlatformOfflineDecorator():
    def __init__(self, platform):
        self.platform = platform
        self.count_of_downloads = 0

    def download_stream(self, stream_reference):
        stream = self.platform.download_stream(stream_reference)
        self.count_of_downloads = self.count_of_downloads + 1

        if self.count_of_downloads >= 10:
            stream['is_online'] = False
        return stream