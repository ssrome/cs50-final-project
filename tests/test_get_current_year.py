import pytest
from datetime import date

from src.get_current_year import GetCurrentYear


@pytest.fixture
def get_current_year():
    return GetCurrentYear()


def test_year_is_not_none(get_current_year):
    response = get_current_year()
    assert response is not None


def test_current_year(get_current_year):
    current_year = date.today().strftime("%Y")
    response = get_current_year()
    assert current_year in response
