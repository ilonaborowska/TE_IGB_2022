# homework no.2: create positive and negative tests for main python types: int, float, bool, strings, lists, tuples, dicts

def if_type_correct(provided_input):
    return type(provided_input)

def test_check_if_int():
    assert if_type_correct(69) == int


def test_check_if_float():
    assert if_type_correct(9.0000001) == float


def test_check_if_boolen():
    assert if_type_correct(False) == bool


def test_check_if_string():
    assert if_type_correct("striny string") == str


def test_check_if_list():
    assert if_type_correct(["trututu", "fafafa", "?", 10]) == list


def test_check_if_dict():
    assert if_type_correct({"Mouse": "tiny", "Elephant": "big"}) == dict


def test_check_if_tuple():
    assert if_type_correct((1,2,3)) == tuple


def test_check_if_true():
    assert 1 + 1 == 2


def test_check_if_false():
    assert "house" != "home"
