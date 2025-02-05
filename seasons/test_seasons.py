from seasons import calculate_days
import pytest


def test_one_year_ago():
    calculate_days("2022-10-22") == "five hundred twenty-five thousand, six hundred".capitalize()

def test_bad_time():
    with pytest.raises(SystemExit):
        calculate_days("33-22-11")

def test_text_date_bad():
     with pytest.raises(SystemExit):
        calculate_days("January 1, 1999")
