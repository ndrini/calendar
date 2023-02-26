import datetime
from unittest.mock import patch
import pytz
from core.day_list import DayList


def mocked_get_now(month=5, day=26):
    local_tz = pytz.timezone("Europe/Paris")
    dt = datetime.datetime(2024, month, day, 10, 10, 10)
    return local_tz.localize(dt)


def test_actual_month():
    """
    https://stackoverflow.com/questions/13073281/how-to-mock-pythons-datetime-now-in-a-class-method-for-unit-testing
    """
    with patch("core.day_list.DayList.get_now", side_effect=mocked_get_now):
        d = DayList()
        assert d.month == 5


def test_get_monthly_day_list():
    pass

def test_select_month():
    """ requests that are close to the end of the month provide next month as result """
    
    with patch("core.day_list.DayList.get_now", side_effect=mocked_get_now):
        d = DayList()
        assert d.select_month() == (2024, 6)


    with patch("core.day_list.DayList.get_now", return_value=mocked_get_now(month=12, day=26)):
        d = DayList()
        assert d.select_month() == (2025, 1)

    # with patch("core.day_list.DayList.get_now", return_value=mocked_get_now(month=12, day=26)):
    #     # d = DayList(offset=-1)
    #     # assert d.select_month() == (2024, 6)
