from src.date_and_time import DateAndTime
import pytest


def date_and_time():
    return DateAndTime()


def test_return_is_not_none():
    assert date_and_time.get_current_year() is not None
