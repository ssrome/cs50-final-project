from src.delete import Delete
from src.update_complete_status import UpdateCompleteStatus
from src.update_edit_status import UpdateEditStatus


class Events:
    def __init__(self):
        self.update_complete_status = UpdateCompleteStatus()
        self.update_edit_status = UpdateEditStatus()
        self.delete = Delete()

    def __call__(self, item_list, index, method, form):
        if method == "POST":
            if "complete-event" in form:
                response = self.update_complete_status(item_list, "complete-event", index)
                return response
            elif "incomplete-event" in form:
                response = self.update_complete_status(item_list, "incomplete-event", index)
                return response
            elif "edit-event" in form:
                response = self.update_edit_status(item_list, "edit-event", index)
                return response
            elif "save-event" in form:
                response = self.update_edit_status(item_list, "save-event", index)
                return response
            elif "delete-event" in form:
                response = self.delete.delete_item(item_list, index)
                return response
            elif "delete-all-event" in form:
                response = self.delete.delete_all(item_list)
                return response
        return item_list
