from um import count

def test_count1():
    assert count("um um, um") == 3

def test_count2():
    assert count("sum um") == 1

def test_count3():
    assert count("What the UM?") == 1

