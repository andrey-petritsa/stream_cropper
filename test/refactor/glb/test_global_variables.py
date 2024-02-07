import unittest

import refactor.glb.global_service as global_service
from refactor.glb.mock_service import MockService
from refactor.glb.service_client import ServiceClient


class TestGlobalVariable(unittest.TestCase):
    def test_with_real_service(self):
        global_service.service = global_service.GlobalService()
        client = ServiceClient()
        self.assertEqual('hello', client.call_service())

    def test_with_mock_service(self):
        global_service.service = MockService()
        client = ServiceClient()
        self.assertEqual('bonjour', client.call_service())