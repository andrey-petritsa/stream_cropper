class StubCheckOnlineStrategy:
    is_online_response = True

    def check_is_online(self, platform_name, stream_reference):
        return self.is_online_response