from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("shazam") == "shzm"
    assert shorten("AExIOU") == "x"
    assert shorten("123456789") == "123456789"
    assert shorten(".,!@?") == ".,!@?"