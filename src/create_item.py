import uuid
from src.date_and_time import DateAndTime


class CreateItem:

    def __init__(self, item_name):
        item_id = uuid.uuid4().int
        self.id = item_id
        self.name = item_name
        self.is_complete = False
        self.is_edit = False
        self.created_at = str(DateAndTime.get_utc_time())

    def create_new_item(self):
        item = {
            "id": self.id,
            "name": self.name,
            "is_complete": self.is_complete,
            "is_edit": self.is_edit,
            "created_at": self.created_at
        }
        return item

    def create_new_countdown_item(self, countdown_date):
        countdown_item = {
            "id": self.id,
            "name": self.name,
            "is_complete": self.is_complete,
            "is_edit": self.is_edit,
            "created_at": self.created_at,
            "countdown_timestamp": DateAndTime.convert_to_utc_time(countdown_date)
        }
        return countdown_item
