import uuid


class EventItem:

    def __init__(self, item_name):
        item_id = uuid.uuid4().int
        self.id = item_id
        self.name = item_name
        self.is_complete = False
        self.is_edit = False

    def create_new_event(self):
        event = {
            "id": self.id, "name": self.name, "is_complete": self.is_complete, "is_edit": self.is_edit
        }
        return event
