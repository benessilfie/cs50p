from um import count


def test_default():
    assert count("hello, um, world") == 1
    assert count("um?") == 1
    assert count("um") == 1


def test_no_um():
    assert count("hello, world") == 0


def test_multiple():
    assert count("um, um, um, um, um, um") == 6


def test_case_insensitive():
    assert count("um, Um, uM, UM") == 4


def test_um_in_word():
    assert count("umbrella") == 0
    assert count("yummy") == 0


def test_um_with_whitespace():
    assert count(" um ") == 1
