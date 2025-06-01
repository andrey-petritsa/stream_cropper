from mocks.platform.local_platform import LocalPlatform
from twith_platform.twith.streamlink_check_online_strategy import StreamlinkCheckOnlineStrategy
from twith_platform.twith.twith import Twith


class PlatformFactory():
    @classmethod
    def create_platform(cls, stream_link):
        if 'twitch' in stream_link:
            return Twith(StreamlinkCheckOnlineStrategy())

        if 'local' in stream_link:
            return LocalPlatform()
