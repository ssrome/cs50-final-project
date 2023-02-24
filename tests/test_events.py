from unittest.mock import MagicMock
from src.events import Events
from tests.fixtures.item_list_response import ONE_COMPLETE_TRUE, ONE_EDIT_TRUE
import pytest

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

request = MagicMock()
request.method = "POST"
request_form_with_complete_event = {"complete-event": "0"}
request_form_with_incomplete_event = {"incomplete-event": "0"}
request_form_with_edit_event = {"edit-event": "0"}
request_form_with_save_event = {"edit-item": "psycho", "save-event": "0"}
request_form_with_delete_event = {"delete-event": "0"}
request_form_with_delete_all_event = {"delete-all-event": "Delete all"}


@pytest.fixture
def events():
    return Events()


def test_return_is_not_none(events):
    response = events(ITEM_LIST, 0, "POST", request_form_with_complete_event)
    assert response is not None
    assert type(response) == list


def test_it_calls_update_complete_status_with_complete_event(events):
    response = events(ITEM_LIST, "POST", request_form_with_complete_event, 0)
    assert response[0]["is_complete"] is True


def test_it_calls_update_complete_status_with_incomplete_event(events):
    response = events(ONE_COMPLETE_TRUE, "POST", request_form_with_incomplete_event, 0)
    assert response[0]["is_complete"] is False


def test_it_calls_update_edit_status_with_edit_event(events):
    response = events(ITEM_LIST, "POST", request_form_with_edit_event, 0)
    assert response[0]["is_edit"] is True


def test_it_calls_update_item_and_update_edit_status_with_save_event(events):
    response = events(ONE_EDIT_TRUE, "POST", request_form_with_save_event, 0)
    assert response[0]["name"] == "psycho"
    assert response[0]["is_edit"] is False


def test_it_calls_delete_item(events):
    response = events(ITEM_LIST, "POST", request_form_with_delete_event, 0)
    assert response[0]["id"] != 1


def test_it_calls_delete_all(events):
    response = events(ITEM_LIST, "POST", request_form_with_delete_all_event)
    assert response == []
