from src.event_item import EventItem


def test_event_is_not_none():
    new_event = EventItem("test1")
    assert new_event is not None
    assert new_event.name == "test1"


def test_event_id():
    new_event = EventItem("test2")
    assert new_event.id is not None
    assert type(new_event.id) == int


def test_event_dict():
    new_event_dict = EventItem("test3").create_new_event()
    assert type(new_event_dict["id"]) == int
    assert new_event_dict["name"] == "test3"
