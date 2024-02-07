from mocks.interactor.in_memory_stream_gateway import InMemoryStreamGateway


class InMemoryGatewayFactory():
    def __init__(self):
        self.stream_gateway = InMemoryStreamGateway()

    def create_stream_gateway(self):
        return self.stream_gateway