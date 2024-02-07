import datetime


class WeightBuilder():
    def build(self, stream_analyze):
        weights = []
        self.first_message = stream_analyze['info']['first_message']
        for explosion in stream_analyze['explosions']:
            weights.append(self.build_weight(explosion))

        sortedW = sorted(weights, key=lambda d: d['weight'], reverse=True)
        return sortedW


    def build_weight(self, messages):
        time_in_seconds = self.first_message.distance(messages[0])
        time_delta = str(datetime.timedelta(seconds=time_in_seconds))
        return {'weight': (len(messages)), 'seconds_time': time_in_seconds, 'time_delta': time_delta}