from unittest.mock import MagicMock
from src.date_and_time import DateAndTime
import pytest
import datetime
from freezegun import freeze_time


@pytest.fixture
def date_time_now_mock():
    return MagicMock(return_value=datetime.date(2012, 1, 14))


@pytest.fixture
def date_and_time():
    return DateAndTime()


@freeze_time("2012-01-14")
def test_return_date_and_time(date_and_time):
    assert date_and_time.get_date_time_now() == datetime.date(2012, 1, 14)


def test_current_year(date_and_time):
    current_year = datetime.date.today().strftime("%Y")
    response = date_and_time.get_current_year()
    assert response is not None
    assert current_year in response


@freeze_time("2010-01-14")
def test_return_year(date_and_time):
    assert date_and_time.get_current_year() == "2010"


@freeze_time("2012-01-14 03:21:34", tz_offset=-4)
def test_returns_utc_time(date_and_time):
    response = date_and_time.get_utc_time()
    assert response == "2012-01-13 23:21:34"


def test_converts_time_to_utc(date_and_time):
    local_now = datetime.datetime(2024, 1, 14, 10, 0, 0)
    utc_now = datetime.datetime(2024, 1, 14, 8, 0, 0)
    countdown_time = datetime.datetime.strptime("2024-01-14 14:00:00", "%Y-%m-%d %H:%M:%S")
    response = date_and_time.convert_to_utc_time(local_now, utc_now, countdown_time)
    print(response)
    assert response == "2024-01-14 12:00:00"
