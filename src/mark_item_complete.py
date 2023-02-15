class MarkItemComplete:

    def __call__(self, event_list, index=""):
        if type(index) != int:
            return event_list
        event_list[index]["complete"] = True
        return event_list
