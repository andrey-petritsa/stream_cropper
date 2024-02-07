from datetime import timedelta
from time import perf_counter

import utils.logger


class Benchmark:
    def run(self, cb, benchmark_id):
        time_start = perf_counter()
        response = cb()
        time_end = perf_counter()
        time_duration = time_end - time_start
        time = self.__convert_time_to_seconds_string(time_duration)
        utils.logger.info(f'{benchmark_id} Took {time} seconds')

        return response

    def __convert_time_to_seconds_string(self, time_duration):
        value = timedelta(seconds=time_duration)
        time = value.total_seconds()
        time = round(time, 5)
        return str(time)
