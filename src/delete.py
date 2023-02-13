class Delete:
    @staticmethod
    def delete_item(event_list, index=None):
        if len(event_list) > 0 and index:
            del event_list[index]
            return event_list
        else:
            return event_list

    @staticmethod
    def delete_all(event_list):
        event_list.clear()
        return []
