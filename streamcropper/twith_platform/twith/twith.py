import threading
from datetime import datetime

from bs4 import BeautifulSoup

import utils
from twith_platform.stream_name_slugger import StreamNameSlugger


class Twith:
    def __init__(self, check_online_strategy):
        self.__platform_name = 'twitch.tv'

        self.__check_online_strategy = check_online_strategy
        self.__stream_id_generator = utils.stream_id_generator
        self.__web_client = utils.web_client
        self.__downloaded_streams= []
        self.__name_slugger = StreamNameSlugger()

    def download_stream(self, stream_reference):
        stream = self.__get_stream(stream_reference)
        stream['id'] = self.__stream_id_generator.generate(stream)

        self.__downloaded_streams.append(stream)

        return stream

    def __get_stream(self, stream_reference):
        html_page = self.__get_stream_html_page(stream_reference)

        if self.__is_stream_online(stream_reference):
            stream = self.__get_online_stream(html_page, stream_reference)
        else:
            stream = self.__get_offline_stream(stream_reference)

        stream['messages'] = []
        stream['platform'] = self.__platform_name

        return stream

    def __get_stream_html_page(self, stream_reference):
        url = f"https://www.twitch.tv/{stream_reference}"
        html_page = self.__web_client.get(url)
        return html_page

    def __is_stream_online(self, stream_reference):
        return self.__check_online_strategy.check_is_online(self.__platform_name, stream_reference)

    def __get_online_stream(self, html_page, stream_reference):
        return {
            'is_online': True,
            "streamer": {
                "name": stream_reference
            },
            'name': self.__get_stream_name(html_page),
            "started_at": datetime.now(),
            "stream_reference": stream_reference
        }

    def __get_offline_stream(self, stream_reference):
        return {
            "is_online": False,
            "streamer": {
                "name": stream_reference
            },
            "name": 'stream offline',
            "started_at": datetime.now(),
            "stream_reference": stream_reference
        }

    def __get_stream_name(self, html_page):
        soup = BeautifulSoup(html_page, features="html.parser")
        stream_name_tag = soup.find("meta", property="og:description")
        return self.__name_slugger.slug(stream_name_tag["content"])

    def get_platform_name(self):
        return 'twith'

    def download_streams(self, stream_references):
        self.__downloaded_streams = []

        download_streams_tasks = []
        for reference in stream_references:
            task = threading.Thread(target=self.download_stream, args=(reference,))
            task.start()
            download_streams_tasks.append(task)

        for task in download_streams_tasks:
            task.join()

        return self.__downloaded_streams
