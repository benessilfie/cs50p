from plates import is_valid


def test_default():
    assert is_valid("CS50") == True


def test_too_short():
    assert is_valid("A") == False


def test_too_long():
    assert is_valid("AB12345") == False


def test_no_letters():
    assert is_valid("1234") == False


def test_no_numbers():
    assert is_valid("AB") == True


def test_number_placemnet():
    assert is_valid("CS50P") == False


def test_zero_placement():
    assert is_valid("CS05") == False


def test_length():
    assert is_valid("H") == False


def test_symbols():
    assert is_valid("PI3.14") == False
