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


# def test_read_user_preference(monkeypatch):
#     input_values = [3, "giovedì", 14]

#     def mock_input(s):
#         output.append(s)
#         return input_values.pop(0)

#     read_user_preference.input = mock_input

#     # monkeypatch.setattr('builtins.input', 
#     #     lambda _: "Mark")

#     read_user_preference.print = lambda s : output.append(s)
#     read_user_preference.main()
 
#     assert output["month"] == "Aprile"