import pytest
from core.text_creator import TextCreator
from core.text_creator import read_user_preference, set_up_environment


# def test_TextCreator():
#     ''' 
#     evaluate the presence of the selected month 
#     in the formatted output text 
#     '''
#     data = set_up_environment()
#     my_c = TextCreator(
#         6, # "giugno" 
#         "martedì", 
#         23,
#         data)
#     result = my_c.export_as_text()
#     print(result)
#     assert result[-10:-1] == "giugno **"


testdata = [(["it", "6", "martedì", "22"],
            {"lang": "it",
             "month": 6,    
             "week_day" : "martedì", 
             "week_number": 22,
             }
            ),
            (["it", "9", "domenica", "45"],
            {"lang": "it",
             "month": 9,    
             "week_day" : "domenica", 
             "week_number": 45,
             }
            ),
            ]

@pytest.mark.parametrize("moke_values,expected", testdata)
def test_read_many(monkeypatch, moke_values, expected):
    values = moke_values
    def substitution(s):
        return values.pop(0)
    monkeypatch.setattr('builtins.input', substitution)
    assert read_user_preference() == expected


def test_set_up_environment():
    data = set_up_environment()
    # print(data)
    print(type(data))
    assert len(data) == 3
    assert "Spanish" in [data[i]['language'] for i in data]
