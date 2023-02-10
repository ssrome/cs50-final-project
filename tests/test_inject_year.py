import pytest as pytest

from src.inject_year import GetYear


@pytest.fixture
def inject_year():
    return GetYear()


def test_year_is_not_none(inject_year):
    response = inject_year()
    assert response is not None
