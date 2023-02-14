import pytest
from datetime import date

from src.inject_year import InjectYear


@pytest.fixture
def inject_year():
    return InjectYear()


def test_year_is_not_none(inject_year):
    response = inject_year()
    assert response is not None


def test_start_year(inject_year):
    response = inject_year()
    assert "2022" in response


def test_current_year(inject_year):
    current_year = date.today().strftime("%Y")
    response = inject_year()
    assert current_year in response
