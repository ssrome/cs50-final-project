import pytest

from src.update_complete_status import UpdateCompleteStatus


ALL_FALSE = [
    {
        "id": 1,
        "is_complete": False,
        "is_edit": False
    },
    {
        "id": 2,
        "is_complete": False,
        "is_edit": False
    }
]

ONE_COMPLETE_TRUE = [
    {
        "id": 1,
        "is_complete": True,
        "is_edit": False
    },
    {
        "id": 2,
        "is_complete": False,
        "is_edit": False
    }
]


@pytest.fixture
def update_complete_status():
    return UpdateCompleteStatus()


def test_returns_list_when_no_index_sent(update_complete_status):
    response = update_complete_status(ALL_FALSE, "complete-event")
    print(response)
    assert type(response) == list
    assert response[0]["is_complete"] is False
    assert response[1]["is_complete"] is False


def test_returns_list_with_one_marked_complete(update_complete_status):
    index = 1
    response = update_complete_status(ALL_FALSE, "complete-event", index)
    assert response[index]["is_complete"] is True


def test_returns_list_with_completed_item_no_longer_complete(update_complete_status):
    index = 0
    response = update_complete_status(ONE_COMPLETE_TRUE, "incomplete-event", index)
    assert response[index]["is_complete"] is False
