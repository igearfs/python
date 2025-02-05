from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75

    with pytest.raises(ZeroDivisionError):
        assert convert("3/0")

    with pytest.raises(ValueError):
        assert convert("3/2")

    with pytest.raises(ValueError):
        assert convert("cat/dog")

def test_gauge():
    assert gauge(convert("3/4")) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"