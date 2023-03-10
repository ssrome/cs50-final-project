import pytest
from src.update_edit_status import UpdateEditStatus
from tests.fixtures.item_list_response import ONE_EDIT_TRUE

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
index = 0


@pytest.fixture()
def update_edit_status():
    return UpdateEditStatus()


def test_return_is_not_none(update_edit_status):
    response = update_edit_status(ITEM_LIST, "edit-event")
    assert response is not None


def test_returns_list_when_no_index_sent(update_edit_status):
    response = update_edit_status(ITEM_LIST, "edit-event")
    assert type(response) == list
    assert response[0]["is_edit"] is False
    assert response[1]["is_edit"] is False


def test_returns_list_with_one_edit_true(update_edit_status):
    response = update_edit_status(ITEM_LIST, "edit-event", index)
    assert response[index]["is_edit"] is True


def test_returns_list_with_edit_item_false_that_was_previously_true(update_edit_status):
    response = update_edit_status(ONE_EDIT_TRUE, "save-event", index)
    assert response[index]["is_edit"] is False
