import unittest

import interactor.factories as factories
from gui.stream_presenter import StreamPresenter
from interactor.use_cases.show_stream_command import ShowStreamCommand
from mocks.interactor.in_memory_gateway_factory import InMemoryGatewayFactory
from mocks.interactor.in_memory_stream_gateway import InMemoryStreamGateway
from test_helpers.stream_builder import StreamBuilder


class TestShowStreamCommand(unittest.TestCase):
    def setUp(self):
        self.init_stream_gateway()
        self.command = ShowStreamCommand(StreamPresenter())
        self.moment_radius = 1

    def init_stream_gateway(self):
        self.stream_gateway = InMemoryStreamGateway()
        factories.gateway_factory = InMemoryGatewayFactory()
        factories.gateway_factory.stream_gateway = self.stream_gateway
        stream_builder = StreamBuilder()
        stream_builder.build_stream()
        self.stream_gateway.save(stream_builder.get_stream())

    def test_show_stream_by_id(self):
        stream = self.command.execute("aaaa-bbbb-cccc-dddd", self.moment_radius)
        self.assertEqual("aaaa-bbbb-cccc-dddd", stream['id'])

    def test_stream_moments_calculated(self):
        stream = self.command.execute("aaaa-bbbb-cccc-dddd", self.moment_radius)

        first_moment = stream['moments'][0]
        self.assertEqual('2', first_moment['weight'])
        self.assertEqual("2011-11-04 12:00:00", first_moment['start'])
