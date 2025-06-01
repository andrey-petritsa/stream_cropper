import threading
from datetime import datetime

from bs4 import BeautifulSoup

import utils
from interactor.stream_watcher.stream_reference_extractor import StreamerNameExtractor
from twith_platform.stream_name_slugger import StreamNameSlugger


class Twith:
    def __init__(self, check_online_strategy):
        self.__check_online_strategy = check_online_strategy
        self.__stream_id_generator = utils.stream_id_generator
        self.__web_client = utils.web_client
        self.__downloaded_streams= []
        self.__name_slugger = StreamNameSlugger()

    def download_stream(self, stream_link):
        stream = self.__get_stream(stream_link)
        stream['id'] = self.__stream_id_generator.generate(stream)

        self.__downloaded_streams.append(stream)

        return stream

    def __get_stream(self, stream_link):
        html_page = self.__get_stream_html_page(stream_link)
        stream = self.__get_stream_meta(stream_link)
        if stream['is_online']:
            stream['name'] = self.__get_stream_name(html_page)

        return stream

    def __get_stream_html_page(self, stream_link):
        html_page = self.__web_client.get(stream_link)
        return html_page

    def __is_stream_online(self, stream_link):
        return self.__check_online_strategy.check_is_online(stream_link)

    def __get_stream_meta(self, stream_link):
        return {
            "streamer": {"name": StreamerNameExtractor.get(stream_link)},
            "started_at": datetime.now(),
            'link': stream_link,
            'is_online': self.__is_stream_online(stream_link),
            'platform' : 'twitch',
            'name': 'offline'
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
