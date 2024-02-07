import unittest

from gui.stream_presenter import StreamPresenter
from interactor import factories
from interactor.use_cases.show_all_streams_info_command import ShowAllStreamsInfoCommand
from mocks.interactor.in_memory_gateway_factory import InMemoryGatewayFactory
from mocks.interactor.in_memory_stream_gateway import InMemoryStreamGateway
from test_helpers.stream_builder import StreamBuilder


class TestShowAllStreamsInfoCommand(unittest.TestCase):
    def setUp(self):
        self.init_stream_gateway()
        self.command = ShowAllStreamsInfoCommand(StreamPresenter())

    def init_stream_gateway(self):
        self.stream_gateway = InMemoryStreamGateway()
        factories.gateway_factory = InMemoryGatewayFactory()
        factories.gateway_factory.stream_gateway = self.stream_gateway
        stream_builder = StreamBuilder()
        stream_builder.build_stream()
        self.stream_gateway.save(stream_builder.get_stream())

    def tearDown(self):
        pass

    def test_stream_id_showed(self):
        streams = self.command.execute()

        self.assertEqual('aaaa-bbbb-cccc-dddd', streams[0]['id'])
