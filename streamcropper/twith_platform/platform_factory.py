from mocks.platform.local_platform import LocalPlatform
from test_helpers.platform_offline_decorator import PlatformOfflineDecorator
from twith_platform.twith.streamlink_check_online_strategy import StreamlinkCheckOnlineStrategy
from twith_platform.twith.twith import Twith


class PlatformFactory():
    def create_platform(self, platform_name):
        if platform_name == 'local':
            return LocalPlatform()

        if platform_name == 'twith':
            return Twith(StreamlinkCheckOnlineStrategy())

        if platform_name == 'twith-testable':
            return PlatformOfflineDecorator(StreamlinkCheckOnlineStrategy())
