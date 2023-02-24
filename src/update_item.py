class UpdateItem:

    @staticmethod
    def __call__(item_list, edit_name, index):
        if type(item_list) == list:
            item_list[index]["name"] = edit_name
            print(item_list)
            return item_list
        return item_list
