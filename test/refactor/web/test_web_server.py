import threading
import unittest

import requests
from interactor.utils import WebServer


class WebServerTest(unittest.TestCase):
    event = threading.Event()

    def kill_socket(self):
        pass

    def sendRequest(self, url):
        myobj = {'somekey': 'somevalue'}
        response = requests.get(url, json = myobj)
        print(response.request.url)
        print(response.request.body)
        print(response.request.headers)
        return response.text

    @classmethod
    def setUpClass(self):
        server = WebServer(self.event)
        threading.Thread(target=server.listen, daemon=True).start()

    def test_send_request(self):
        response = self.sendRequest('https://jsonplaceholder.typicode.com/todos/1')
        self.assertTrue(response != "")

    @unittest.skip
    def test_server_with_requests_lib(self):
        response1 = self.sendRequest('http://localhost:1234')
        response2 = self.sendRequest('http://localhost:1234')

        self.assertEqual('Hello World!', response1)
        self.assertEqual('Hello World!', response2)

