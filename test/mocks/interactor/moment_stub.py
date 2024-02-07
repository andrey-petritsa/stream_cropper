from datetime import datetime


class MomentStub():
    def __init__(self, weight, moment_start_iso):
        self.weight = weight
        self.start = datetime.fromisoformat(moment_start_iso)

    def get_weight(self):
        return self.weight

    def get_start(self):
        return self.start

    def get_end(self):
        return self.start

    def __str__(self):
        return str(f'weight: {self.weight}')