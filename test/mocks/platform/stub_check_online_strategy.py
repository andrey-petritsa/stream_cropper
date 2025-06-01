class StubCheckOnlineStrategy:
    is_online_response = True

    def check_is_online(self, stream_link):
        return self.is_online_response