from twith_platform import Twith
from twith_platform.twith.streamlink_check_online_strategy import StreamlinkCheckOnlineStrategy


class TwithStreamFinder():
    def __init__(self):
        self.__platform = self._create_platform()

    def find_online_stream(self):
        streams = self.__platform.download_streams(self._get_stream_references())
        for stream in streams:
            if stream['is_online']:
                return stream

        raise Exception('Online stream not founded')

    def _create_platform(self):
        return Twith(StreamlinkCheckOnlineStrategy())

    def _get_stream_references(self):
        return [
            'https://twitch.tv/unclebjorn',
            'https://twitch.tv/igorghk',
            "https://twitch.tv/lenagol0vach",
            'https://twitch.tv/welovegames',
            'https://twitch.tv/orkpod',
            'https://twitch.tv/vika_karter',
            'https://twitch.tv/bigrussianmum',
            'https://twitch.tv/kosmeya',
            'https://twitch.tv/evikey',
            'https://twitch.tv/faridysha',
            'https://twitch.tv/juice',
            'https://twitch.tv/sofiko_sculpts',
            "https://twitch.tv/dmitry_bale",
            "https://twitch.tv/dreadztv"
        ]