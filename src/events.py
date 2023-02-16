from localStoragePy import localStoragePy

from src.update_complete_status import UpdateCompleteStatus

localStorage = localStoragePy("cs50-todo", "text")


class Events:
    def __init__(self, update_complete_status: UpdateCompleteStatus):
        self.update_complete_status = update_complete_status

    def __call__(self, events, index, method, form):
        if method == "POST":
            if "complete-event" in form:
                response = self.update_complete_status(events, index)
                return response
        return events
