from src.create_item import CreateItem


def test_event_is_not_none():
    new_item = CreateItem("test1")
    assert new_item is not None
    assert new_item.name == "test1"


def test_event_id():
    new_item = CreateItem("test2")
    assert new_item.id is not None
    assert type(new_item.id) == int


def test_event_dict():
    new_item_dict = CreateItem("test3").create_new_item()
    assert type(new_item_dict["id"]) == int
    assert new_item_dict["name"] == "test3"
    assert new_item_dict["is_complete"] is False
    assert new_item_dict["is_edit"] is False
    assert type(new_item_dict["created_at"]) == str


def test_create_countdown_item():
    new_item_dict = CreateItem("Celebrate").create_new_countdown_item()
    assert new_item_dict is not None
    assert type(new_item_dict["id"]) == int
    assert new_item_dict["name"] == "Celebrate"
    assert new_item_dict["is_complete"] is False
    assert new_item_dict["is_edit"] is False
    assert type(new_item_dict["created_at"]) == str


# test it takes date and time and returns in dict
# test it take date and defaults time to 0:0
# date is required. time isn't
#def test_returns_
