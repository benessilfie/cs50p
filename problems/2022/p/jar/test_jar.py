from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    try:
        jar = Jar(-1)
        assert False, "Expected ValueError for negative capacity"
    except ValueError:
        pass


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

    try:
        jar.deposit(10)
        assert False
    except ValueError:
        pass

    try:
        jar.deposit(13)
        assert False
    except ValueError:
        pass


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    assert str(jar) == "🍪🍪"

    try:
        jar.withdraw(5)
        assert False
    except ValueError:
        pass

