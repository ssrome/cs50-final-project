import uuid


class EventItem:

    def __init__(self, event_name):
        event_id = uuid.uuid4().int
        self.id = event_id
        self.name = event_name
