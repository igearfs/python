from jar import Jar
import pytest

def test_init():
    j = Jar()
    assert j.capacity == 12
    j = Jar(55)
    assert j.capacity == 55
    with pytest.raises(ValueError):
        j = Jar(-10)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.deposit(55)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.withdraw(55)