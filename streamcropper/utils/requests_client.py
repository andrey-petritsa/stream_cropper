import logging

import requests


class RequestsClient:
    def __init__(self):
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

    def get(self, url, need_meta=False):
        response = requests.get(url)
        response.encoding = 'utf-8'
        if need_meta:
            return response
        return response.text
