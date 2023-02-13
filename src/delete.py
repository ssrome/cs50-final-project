class Delete:
    @staticmethod
    def delete_item(event_list, index):
        if len(event_list) > 0:
            event_list.pop(index)
            return event_list
        else:
            return event_list

    @staticmethod
    def delete_all(event_list):
        event_list.clear()
        return event_list
