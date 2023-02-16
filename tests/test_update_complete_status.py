import pytest

from src.update_complete_status import UpdateCompleteStatus

EVENT_LIST = [{"id": 1, "complete": False}, {"id": 2, "complete": False}]


@pytest.fixture
def update_complete_status():
    return UpdateCompleteStatus()


def test_returns_a_list(update_complete_status):
    response = update_complete_status(EVENT_LIST, 0)
    assert type(response) == list


def test_returns_list_when_no_index_sent(update_complete_status):
    response = update_complete_status(EVENT_LIST)
    assert '"complete": True' not in response


def test_returns_list_with_one_marked_complete(update_complete_status):
    index = 1
    response = update_complete_status(EVENT_LIST, index)
    assert response[index]["complete"] is True
