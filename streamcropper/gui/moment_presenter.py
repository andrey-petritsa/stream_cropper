
class MomentPresenter():
    def format_moments(self, stream):
        view_moments = []
        for moment in stream['moments']:
            view_moment = {
                'weight': str(moment.get_weight()),
                'delta': {
                    'start': self.__format_start_delta(moment, stream['started_at']),
                    'end': self.__format_end_delta(moment, stream['started_at'])
                },
                'delta_sec': {
                    'start': self.__format_sec_start_delta(moment, stream['started_at']),
                    'end': self.__format_sec_end_delta(moment, stream['started_at']),
                },
                'start': str(stream['started_at'])
            }
            view_moments.append(view_moment)
        return view_moments


    def __format_start_delta(self, moment, stream_start_at):
        return str(moment.get_start() - stream_start_at)

    def __format_end_delta(self, moment, stream_start_at):
        return str(moment.get_end() - stream_start_at)

    def __format_sec_start_delta(self, moment, stream_start_at):
        timeDiff = moment.get_start() - stream_start_at
        return str(timeDiff.total_seconds())

    def __format_sec_end_delta(self, moment, stream_start_at):
        timeDiff = moment.get_end() - stream_start_at
        return str(timeDiff.total_seconds())