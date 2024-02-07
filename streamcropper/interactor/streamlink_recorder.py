import subprocess

import utils


class StreamlinkRecorder():
    def __init__(self):
        self.__process = None
        self.__platform = None
        self.__output = None

    def start(self, stream_link):
        stream_link = f"{self.__platform}/{stream_link}"

        self.__cmd = f"streamlink --force --output {self.__output} {stream_link} worst"
        self.__process = subprocess.Popen(self.__cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        utils.logger.info(f'Streamlink record started | {self.__cmd}')

    def stop(self):
        self.__process.terminate()
        (stdout, stderr) = self.__process.communicate()
        utils.logger.info(f'Streamlink record stopped | {self.__cmd}')

    def set_output(self, output):
        self.__output = output

    def set_platform(self, platform):
        self.__platform = platform

