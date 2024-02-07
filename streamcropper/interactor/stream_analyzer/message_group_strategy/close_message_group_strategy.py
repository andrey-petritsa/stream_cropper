class CloseMessageGroupStrategy():
    def group_messages(self, messages, radius):
        if (len(messages) == 0):
            return []

        message_groups = []
        message_group = []
        reference = messages[0]
        for i, moment in enumerate(messages):
            if(i == 0):
                message_group.append(messages[0])

            if (i + 1 >= len(messages)):
                message_groups.append(message_group)
                break

            if reference.distance(messages[i + 1]) <= radius:
                message_group.append(messages[i + 1])
            else:
                message_groups.append(message_group)
                message_groups.extend(self.group_messages(messages[i + 1:], radius))
                break

        return message_groups