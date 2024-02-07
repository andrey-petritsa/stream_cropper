class StubWebClient():
    response = None

    def get(self, url):
        return self.response