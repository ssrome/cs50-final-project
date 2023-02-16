from unittest.mock import MagicMock
from src.events import Events
import pytest


EVENT_LIST = [{"id": 1, "complete": False}, {"id": 2, "complete": False}]

EVENT_LIST_RESPONSE = [{"id": 1, "complete": False}, {"id": 2, "complete": True}]


request = MagicMock()
request.method = "POST"
request_form = {"complete-event": "0"}


@pytest.fixture()
def update_complete_status_mock():
    return MagicMock()


@pytest.fixture
def events(update_complete_status_mock):
    return Events(update_complete_status_mock)


def test_return_is_not_none(events):
    response = events(EVENT_LIST, 1, "POST", request_form)
    assert response is not None


def test_it_calls_mark_items_complete(update_complete_status_mock, events):
    events(EVENT_LIST, 1, "POST", request_form)
    update_complete_status_mock.assert_called()


def test_it_calls_mark_items_complete_with_events_list(update_complete_status_mock, events):
    events(EVENT_LIST, 1, "POST", request_form)
    update_complete_status_mock.assert_called_with(EVENT_LIST, "complete-event", 1)


def test_events_returns_a_list(update_complete_status_mock, events):
    update_complete_status_mock.return_value = EVENT_LIST_RESPONSE
    response = events(EVENT_LIST, 1, "POST", request_form)
    assert type(response) == list


def test_doesnt_call_mark_items_complete_with_post_method_and_edit_event(update_complete_status_mock, events):
    events(EVENT_LIST, 1, "POST", {"edit-event": "0"})
    update_complete_status_mock.assert_not_called()
