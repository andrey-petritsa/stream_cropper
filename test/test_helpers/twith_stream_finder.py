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
            "lenagol0vach",
            'welovegames',
            'orkpod',
            'vika_karter',
            'bigrussianmum',
            'igorghk',
            'unclebjorn',
            'kosmeya',
            'evikey',
            'faridysha',
            'juice',
            'sofiko_sculpts',
            "dmitry_bale",
            "dreadztv"
        ]