import pytest
from text_creator import TextCreator
from text_creator import read_user_preference

def test_TextCreator():
    my_c = TextCreator(
        6, # "Giugno" 
        "martedì", 
        23,
       )
    result = my_c.export_as_text()
    assert result[-10:-1] == "Giugno **"


testdata = [(["6", "martedì", "22"],
            {"month": 6,    
             "week_day" : "martedì", 
             "week_number": 22,
             }
            ),
            (["9", "domenica", "45"],
            {"month": 9,    
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