from fuel import convert, gauge
from pytest import raises as rs


def test_default_convert():
    assert convert("1/2") == 50


def test_default_gauge():
    assert gauge(50) == "50%"


def test_convert_empty():
    assert convert("0/4") == 0
    assert convert("1/100") == 1


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_convert_full():
    assert convert("4/4") == 100
    assert convert("99/100") == 99


def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_zero_division():
    with rs(ZeroDivisionError):
        convert("4/0")


def test_value_error():
    with rs(ValueError):
        convert("three/four")
        convert("1.5/3")
