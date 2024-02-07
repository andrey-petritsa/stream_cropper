from interactor.stream_analyzer.moment import Moment


class MomentFinder():
    def __init__(self, close_message_group_strategy):
        self.close_message_group_strategy = close_message_group_strategy

    def find(self, stream, moment_radius):
        message_groups = self.close_message_group_strategy.group_messages(stream['messages'], moment_radius)
        moments = self.__convert_message_groups_to_moments(message_groups)

        return moments

    def __convert_message_groups_to_moments(self, message_groups):
        moments = []
        for messages in message_groups:
            moments.append(Moment(messages))

        return moments
