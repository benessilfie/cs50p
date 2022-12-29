from bank import value


def test_default():
    assert value("hello") == 0


def test_value_starts_with_h():
    greeting = "How you doing?"
    assert value(greeting) == 20


def test_value_not_starts_with_h():
    greeting = "What's happening?"
    assert value(greeting) == 100
