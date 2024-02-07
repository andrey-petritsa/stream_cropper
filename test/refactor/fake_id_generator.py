class FakeIdGenerator:
    default_id = "abba"

    def generate(self):
        return self.default_id