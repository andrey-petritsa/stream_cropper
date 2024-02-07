import threading
import time

from interactor.task.record_video_task import RecordVideoTask


def record_some_time(seconds, streamer):
    path_to_video_dir = '/Volumes/hdd_external/stream_cropper/2h'
    ffmpeg = RecordVideoTask(path_to_video_dir)
    ffmpeg.process_id = streamer
    ffmpeg.start(streamer)
    time.sleep(seconds)
    ffmpeg.stop()

streamers = [
    'juice',
    'dangar',
    'sofiko_sculpts',
    'vika_karter',
    "hyver",
    "dmitry_bale",
    "olyavoodoo",
    "orkpod",
]


def start_recording(seconds):
    threads = []
    for streamer in streamers:
        thread = threading.Thread(target=record_some_time, args=(seconds, streamer))
        threads.append({"thread": thread, "name": streamer})
    for thread in threads:
        thread["thread"].start()

    while(True):
        should_end_process = True
        for thread in threads:
            if thread['thread'].is_alive():
                should_end_process = False
                print(f"Поток {thread['name']} еще работает...")
            else:
                print(f"Поток {thread['name']} завершил свою работу")

        if should_end_process:
            print("Все потоки завершили работу")
            return 0
        time.sleep(5)



start_recording(60*120)



