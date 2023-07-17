# py_pytest/tests/unittest_mock/my_calendar/main.py

from typing import Type
from datetime import datetime


def is_weekday(date: Type[datetime] = datetime):
    today = date.today()
    print('today', today)
    # monday = 0, saturday = 6
    return 0 <= today.weekday() < 5


if __name__ == '__main__':
    assert is_weekday()
