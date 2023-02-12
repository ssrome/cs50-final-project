class Delete:
    def delete_item(self, event_list, index=None):
        if len(event_list) > 0 and index:
            del event_list[index]
            return event_list
        else:
            return event_list

    def delete_all(self, event_list):
        event_list.clear()
        return event_list
