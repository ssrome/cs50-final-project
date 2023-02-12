import pytest
from src.delete import Delete


@pytest.fixture()
def delete():
    return Delete()


def test_delete_is_not_none(delete):
    response = delete.delete_item([])
    assert response is not None


def test_delete_returns_a_list(delete):
    response = delete.delete_item([])
    assert type(response) == list


def test_delete_doesnt_return_item_to_delete(delete):
    event_list = [{"id": 1}, {"id": 2}, {"id": 3}]
    event_list_len = len(event_list)
    response = delete.delete_item(event_list, 1)
    assert len(response) == event_list_len - 1
    assert {"id": 2} not in response


def test_delete_all_returns_empty_list(delete):
    event_list = [{"id": 1}, {"id": 2}]
    response = delete.delete_all(event_list)
    assert len(response) == 0
    assert response == []
