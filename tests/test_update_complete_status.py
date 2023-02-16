import pytest

from src.mark_item_complete import MarkItemComplete

EVENT_LIST = [{"id": 1, "complete": False}, {"id": 2, "complete": False}]


@pytest.fixture
def mark_item_complete():
    return MarkItemComplete()


def test_returns_a_list(mark_item_complete):
    response = mark_item_complete(EVENT_LIST, 0)
    assert type(response) == list


def test_returns_list_when_no_index_sent(mark_item_complete):
    response = mark_item_complete(EVENT_LIST)
    assert '"complete": True' not in response


def test_returns_list_with_one_marked_complete(mark_item_complete):
    index = 1
    response = mark_item_complete(EVENT_LIST, index)
    assert response[index]["complete"] is True
