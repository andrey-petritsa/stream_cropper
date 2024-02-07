class MessageSpamStrategy():
    def group_messages(self, messages, radius):
        self.__radius = radius
        groups = []

        if len(messages) == 0:
            return []

        sub_group = []
        for i in range(len(messages)):
            sub_group.append(messages[i])

            if i == len(messages) - 1:
                groups.append(sub_group)
                break

            if self.__messages_too_far(messages[i], messages[i+1]):
                groups.append(sub_group)
                sub_group = []

        return groups

    def __messages_too_far(self, first_message, second_message):
        return first_message.distance(second_message) > self.__radius