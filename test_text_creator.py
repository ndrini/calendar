from text_creator import TextCreator

def test_TextCreator():
    my_c = TextCreator(
        6, # "Giugno" 
        "martedì", 
        23,
       )
    result = my_c.export_as_text()
    assert result[-10:-1] == "Giugno **"


# def test_read_user_preference():
#     my_pref = read_user_preference()
#     assert pref["month"] == "Aprile"