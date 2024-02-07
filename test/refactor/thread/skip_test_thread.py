import subprocess
import threading
import time
import unittest
import uuid

import streamlink
from interactor.utils import QueryThread


class TestProcess(unittest.TestCase):
    def say_hello(self):
        while True:
            self.messageGateway.save('Hello World')
            time.sleep(5)

    def test_thread(self):
        thread = threading.Thread(target=self.say_hello, daemon=True)

        thread.start()
        time.sleep(5)

        self.assertEqual('Hello World', self.messageGateway.messages[0])

    def test_thread_dont_block_main(self):
        threading.Thread(target=self.say_hello).start()
        self.assertEqual('Hello World', self.messageGateway.messages[0])

    def test_run_process(self):
        result = subprocess.run(["ls", "/tmp"], capture_output=True, text=True)
        self.assertNotEqual(result.stdout, '')

    def test_run_ffmpeg_process(self):
        twith_url = 'https://www.twitch.tv/bigrussianmum'
        stream_url = streamlink.streams(twith_url)['best'].url
        filename = str(uuid.uuid4())
        cmd = ["ffmpeg", "-i", stream_url, "-c", "copy", "-t", "5", f"/tmp/{filename}.mkv"]
        subprocess.run(cmd, capture_output=True, text=True)

    def fun1(self):
        time.sleep(6)
        print([1,2,3])

    def fun2(self):
        time.sleep(3)
        print('hello world!')

    def test_sync_two_threads(self):
        threads = [threading.Thread(target=self.fun1), threading.Thread(target=self.fun2)]
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def say_my_name(self):
        return 'andry'

    def test_thread_return_value(self):
        thread = QueryThread(target=self.say_my_name)
        thread.start()
        thread.join()

        self.assertEqual('andry', thread.output)



