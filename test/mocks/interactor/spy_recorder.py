class SpyRecorder:
    accepted_events = []

    def handle_event(self, event):
        self.accepted_events.append(event)

    def get_events_by_streamer(self, name):
        streamer_events = []
        for event in self.accepted_events:
            if(event['stream']['streamer']['name'] == name):
                streamer_events.append(event)

        return streamer_events