import core
import pytest
import datetime
from unittest.mock import Mock, patch
import pytz
from core.day_list import DayList


class mock_datetime:
    month = 2


def mocked_get_now():
    local_tz = pytz.timezone("Europe/Paris")
    dt = datetime.datetime(2023, 5, 1, 10, 10, 10)
    return local_tz.localize(dt)
    

def test_DayList():
    d = DayList()
    assert d.month == 1

# def test_actual_month(mocker):
def test_actual_month():
    # # date = 
    # mocker.patch.object(
    #     'core.day_list.datetime',
    #     mock_datetime
    #     )

    # with patch.object(core.day_list.datetime.datetime, "now") as now_mocked:
    #         now_mocked.return_value = datetime.datetime(2012, 1, 14)

    """
    https://stackoverflow.com/questions/13073281/how-to-mock-pythons-datetime-now-in-a-class-method-for-unit-testing
    """

    with patch("core.day_list.DayList.get_now", side_effect=mocked_get_now) as now_mocked:
        d = DayList()
        assert d.month == 5
