from plates import is_valid

def test_is_valid():
    assert is_valid("AA123")
    assert is_valid("ABCDE")
    assert is_valid("AB")
    assert is_valid("ABAA1")
    assert is_valid("ABA.A1") == False
    assert is_valid("!@#") == False

def test_numbers():
    assert is_valid("12") == False
    assert is_valid("AA12A") == False
    assert is_valid("AA112")
    assert is_valid("CS50")

def test_length():
    assert is_valid("AAAAAAAA") == False
    assert is_valid("A") == False


def test_zero_placement():
    assert is_valid("A0AAA") == False
    assert is_valid("AA0AA") == False
    assert is_valid("AA012") == False