import copy


class MomentSorter:
    def sort_by_weights_ask(self, stream):
        stream_copy = copy.copy(stream)
        sorted_moments = stream_copy['moments']
        sorted_moments.sort(key=self.__get_weight_key, reverse=True)

        return stream_copy

    def __get_weight_key(self, moment):
        return moment.get_weight()
