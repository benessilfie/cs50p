from numb3rs import validate


def main():
    test_default_validate()
    test_validate_empty()
    test_validate_full()
    test_validate_invalid()
    test_validate_range()
    test_validate_string()


def test_default_validate():
    assert validate(r"127.0.0.1") == True
    assert validate(r"127.0.0") == False
    assert validate(r"127.0") == False
    assert validate(r"127") == False


def test_validate_empty():
    assert validate(r"") == False


def test_validate_full():
    assert validate(r"255.255.255.255") == True


def test_validate_invalid():
    assert validate(r"512.512.512.512") == False


def test_validate_range():
    assert validate(r"512.2.3.4") == False
    assert validate(r"1.512.3.4") == False
    assert validate(r"1.2.512.4") == False
    assert validate(r"1.2.3.512") == False


def test_validate_string():
    assert validate(r"cat") == False


if __name__ == "__main__":
    main()
