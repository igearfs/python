from numb3rs import validate



def test_invalid_ip():
    assert validate("2.2.1.299") == False
    assert validate("....") == False
    assert validate("") == False
    assert validate("256.255.255.255") == False
    assert validate("1111.255.255.255") == False
    assert validate("10.10.10.10.10") == False

def test_valid_ip():
    assert validate("255.255.255.255")
    assert validate("12.13.13.13")
    assert validate("0.0.0.0")
    assert validate("01.011.01.10")
    assert validate("001.001.001.001")