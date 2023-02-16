class UpdateCompleteStatus:

    def __call__(self, item_list, button_event, index=""):
        if type(index) != int:
            return item_list

        if button_event == "complete-event":
            item_list[index]["is_complete"] = True
            return item_list

        item_list[index]["is_complete"] = False
        return item_list
