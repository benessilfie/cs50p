from twttr import shorten


def test_default():
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("HELLO") == "HLL"


def test_mixed():
    assert shorten("HeLlO") == "HLl"


def test_empty():
    assert shorten("") == ""


def test_numbers():
    assert shorten("12345") == "12345"


def test_special():
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
