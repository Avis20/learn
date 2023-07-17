# py_pytest/tests/unittest_mock/my_calendar/test.py

from datetime import datetime

from unittest.mock import Mock

from tests.unittest_mock.my_calendar.main import is_weekday

saturday = datetime(year=2023, month=1, day=7)


def test_workday():
    mock_datetime = Mock()
    monday = datetime(year=2023, month=6, day=27)
    mock_datetime.today.return_value = monday
    assert is_weekday(mock_datetime)


def test_off_day():
    mock_datetime = Mock()
    monday = datetime(year=2023, month=7, day=2)
    mock_datetime.today.return_value = monday
    assert not is_weekday(mock_datetime)
