import pytest
from src.update_item import UpdateItem


ITEM_LIST = [
        {
            "id": 1,
            "name": "monster",
            "is_complete": False,
            "is_edit": False
        },
        {
            "id": 2,
            "name": "pose",
            "is_complete": False,
            "is_edit": False
        }
    ]


@pytest.fixture
def update_item():
    return UpdateItem()


def test_updates_name_when_index_is_available(update_item):
    edit_name = "butterflies"
    index = 0
    response = update_item(ITEM_LIST, edit_name, index)
    assert type(response) == list
    assert response[index]["name"] == edit_name
