class Message():
    def __init__(self, datetime, text, user):
        self.datetime = datetime
        self.text = text
        self.user = user

    def distance(self, message):
        thisDate = self.datetime
        anotherDate = message.datetime
        secondDiff = abs((thisDate - anotherDate).total_seconds())

        return secondDiff

    def __eq__(self, message):
        return self.datetime == message.datetime