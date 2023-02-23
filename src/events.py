from src.update_complete_status import UpdateCompleteStatus
from src.update_edit_status import UpdateEditStatus


class Events:
    def __init__(self):
        self.update_complete_status = UpdateCompleteStatus()
        self.update_edit_status = UpdateEditStatus()

    def __call__(self, events, index, method, form):
        if method == "POST":
            if "complete-event" in form:
                response = self.update_complete_status(events, "complete-event", index)
                return response
            elif "incomplete-event" in form:
                response = self.update_complete_status(events, "incomplete-event", index)
                return response
            elif "edit-event" in form:
                response = self.update_edit_status(events, "edit-event", index)
                return response
            elif "save-event" in form:
                response = self.update_edit_status(events, "save-event", index)
                return response
        return events
