class Delete:
    def delete_item(self, event_list):
        if len(event_list) > 0:
            event_list.pop()
            return event_list
        else:
            return event_list

    def delete_all(self, event_list):
        event_list.clear()
        return event_list
