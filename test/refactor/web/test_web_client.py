import threading
import unittest

from utils.web.webclient import WebClient


class WebClientTest(unittest.TestCase):
    client = WebClient()

    @classmethod
    def setUpClass(self):
        server = WebServer(threading.Event())
        threading.Thread(target=server.listen, daemon=True).start()

    def test_send_get_html(self):
        response = self.client.send_get('http://example.com:80/index.html')
        self.assertTrue(response["body"] != "")

    def test_send_get_json(self):
        response = self.client.send_get('http://jsonplaceholder.typicode.com:80/todos/1')
        self.assertTrue(response["body"]["userId"] == 1)

    def test_send_post(self):
        response = self.client.send_post('http://jsonplaceholder.typicode.com:80/posts', {
            "title": 'foo',
            "body": 'bar',
            "userId": 1
        })
        self.assertEqual(response['body']['id'], 101)

    @unittest.skip
    def test_send_https(self):
        response = self.client.send_get('https://lenta.ru:443/news/2023/11/03/ali/')
        self.assertTrue(response["body"] != "")
