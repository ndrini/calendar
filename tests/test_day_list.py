import datetime
from unittest.mock import patch
import pytz
from core.day_list import DayList


def mocked_get_now():
    local_tz = pytz.timezone("Europe/Paris")
    dt = datetime.datetime(2023, 5, 1, 10, 10, 10)
    return local_tz.localize(dt)
    

def test_actual_month():
    """
    https://stackoverflow.com/questions/13073281/how-to-mock-pythons-datetime-now-in-a-class-method-for-unit-testing
    """
    with patch("core.day_list.DayList.get_now", side_effect=mocked_get_now) as now_mocked:
        d = DayList()
        assert d.month == 5

