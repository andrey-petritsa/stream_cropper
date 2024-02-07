from mocks.platform.fake_platform import FakePlatform


class FakePlatformFactory():
    def __init__(self, platform=FakePlatform()):
        self.platform = platform

    def create_platform(self, platform_name):
        return self.platform
