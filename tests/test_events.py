from unittest.mock import MagicMock
from src.events import Events
import pytest


EVENT_LIST = [{"id": 1, "complete": False}, {"id": 2, "complete": False}]

EVENT_LIST_RESPONSE = [{"id": 1, "complete": False}, {"id": 2, "complete": True}]


request = MagicMock()
request.method = "POST"
request_form = {"complete-event": "0"}


@pytest.fixture()
def mark_item_complete_mock():
    return MagicMock()


@pytest.fixture
def events(mark_item_complete_mock):
    return Events(mark_item_complete_mock)


def test_return_is_not_none(events):
    response = events(EVENT_LIST, 1, "POST", request_form)
    assert response is not None


def test_it_calls_mark_items_complete(mark_item_complete_mock, events):
    events(EVENT_LIST, 1, "POST", request_form)
    mark_item_complete_mock.assert_called()


def test_it_calls_mark_items_complete_with_events_list(mark_item_complete_mock, events):
    events(EVENT_LIST, 1, "POST", request_form)
    mark_item_complete_mock.assert_called_with(EVENT_LIST, 1)


def test_events_returns_a_list(mark_item_complete_mock, events):
    mark_item_complete_mock.return_value = EVENT_LIST_RESPONSE
    response = events(EVENT_LIST, 1, "POST", request_form)
    assert type(response) == list


def test_doesnt_call_mark_items_complete_with_post_method_and_edit_event(mark_item_complete_mock, events):
    events(EVENT_LIST, 1, "POST", {"edit-event": "0"})
    mark_item_complete_mock.assert_not_called()
