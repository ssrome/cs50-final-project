class UpdateEditStatus:

    @staticmethod
    def __call__(item_list, button_event, index=None):
        if type(index) != int or index is None:
            return item_list

        if button_event == "edit-event":
            item_list[index]["is_edit"] = True
            return item_list

        item_list[index]["is_edit"] = False
        return item_list
