class StreamerNameExtractor():
    @classmethod
    def get(cls, stream_link):
        return stream_link.split('/')[-1]