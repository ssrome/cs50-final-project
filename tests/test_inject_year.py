import pytest as pytest
from datetime import date

from src.inject_year import InjectYear


@pytest.fixture
def inject_year():
    return InjectYear().inject_year()


def test_year_is_not_none(inject_year):
    response = inject_year
    assert response is not None


def test_start_year(inject_year):
    response = inject_year
    assert "2022" in response


def test_current_year(inject_year):
    today = date.today()
    current_year = today.strftime("%Y")
    response = inject_year
    assert current_year in response
