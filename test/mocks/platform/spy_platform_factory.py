class SpyPlatformFactory():
    def __init__(self):
        self.platform = None
        self.is_called = False

    def create_platform(self, platform_name):
        self.is_called = True
        return self.platform
