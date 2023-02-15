from localStoragePy import localStoragePy

localStorage = localStoragePy("cs50-todo", "text")


class Events:
    def __init__(self, mark_item_complete):
        self.mark_item_complete = mark_item_complete

    def __call__(self, events, index, method, form):
        if method == "POST" and "complete-event" in form:
            response = self.mark_item_complete(events, index)
            return response
        return events

