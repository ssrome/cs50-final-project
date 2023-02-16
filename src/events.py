from src.update_complete_status import UpdateCompleteStatus


class Events:
    def __init__(self, update_complete_status: UpdateCompleteStatus):
        self.update_complete_status = update_complete_status

    def __call__(self, events, index, method, form):
        if method == "POST":
            if "complete-event" in form:
                response = self.update_complete_status(events, "complete-event", index)
                return response
            elif "incomplete-event" in form:
                response = self.update_complete_status(events, "incomplete-event", index)
                return response
        return events
