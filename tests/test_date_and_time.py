from src.date_and_time import DateAndTime
# from unittest.mock import MagicMock
import pytest
import datetime
from freezegun import freeze_time


# @pytest.fixture
# def date_time_now_mock():
#     return MagicMock(return_value=datetime('Jun 1 2017', '%b %d %Y'))


@pytest.fixture
def date_and_time():
    return DateAndTime()


@freeze_time("2012-01-14")
def test_return_is_not_none(date_and_time):
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)

# def test_return_is_not_none(date_and_time):
#     response = date_and_time.get_current_year()
#     assert response is not None

# @freeze_time("2012-01-14")
# def test_current_year(self, date_time_now_mock):
#     date_time_now_mock.date.today = Mock()
#     value = date_and_time.get_current_year()
#     assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)
#     assert "2017" in value
