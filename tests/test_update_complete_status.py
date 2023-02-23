import pytest

from src.update_complete_status import UpdateCompleteStatus
from tests.fixtures.item_list_response import ALL_FALSE

ITEM_LIST = ALL_FALSE


@pytest.fixture
def update_complete_status():
    return UpdateCompleteStatus()


def test_returns_list_when_no_index_sent(update_complete_status):
    response = update_complete_status(ITEM_LIST, "complete-event")
    assert type(response) == list
    assert response[0]["is_complete"] is False
    assert response[1]["is_complete"] is False


def test_returns_list_with_one_marked_complete(update_complete_status):
    index = 1
    response = update_complete_status(ITEM_LIST, "complete-event", index)
    assert response[index]["is_complete"] is True


def test_returns_list_with_completed_item_no_longer_complete(update_complete_status):
    index = 0
    item_list = [{"id": 1, "is_complete": True}]
    response = update_complete_status(item_list, "incomplete-event", index)
    assert response[index]["is_complete"] is False
