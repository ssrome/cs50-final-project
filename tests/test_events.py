from unittest.mock import MagicMock
from src.events import Events
from tests.fixtures.item_list_response import ALL_FALSE, ONE_COMPLETE_TRUE, ONE_EDIT_TRUE
import pytest

ITEM_LIST = ALL_FALSE

request = MagicMock()
request.method = "POST"
request_form_with_complete_event = {"complete-event": "0"}
request_form_with_incomplete_event = {"incomplete-event": "0"}
request_form_with_edit_event = {"edit-event": "0"}
request_form_with_save_event = {"save-event": "0"}


@pytest.fixture
def events():
    return Events()


def test_return_is_not_none(events):
    response = events(ITEM_LIST, 0, "POST", request_form_with_complete_event)
    assert response is not None
    assert type(response) == list


def test_it_calls_update_complete_status_with_complete_event(events):
    response = events(ITEM_LIST, 0, "POST", request_form_with_complete_event)
    assert response[0]["is_complete"] is True


def test_it_calls_update_complete_status_with_incomplete_event(events):
    response = events(ONE_COMPLETE_TRUE, 0, "POST", request_form_with_incomplete_event)
    assert response[0]["is_complete"] is False


def test_it_calls_update_edit_status_with_edit_event(events):
    response = events(ITEM_LIST, 0, "POST", request_form_with_edit_event)
    assert response[0]["is_edit"] is True


def test_it_calls_update_edit_status_with_save_event(events):
    response = events(ONE_EDIT_TRUE, 0, "POST", request_form_with_save_event)
    assert response[0]["is_edit"] is False
