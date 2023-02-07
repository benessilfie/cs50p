from pytest import raises
from seasons import check_date_format


def test_default():
    assert check_date_format("1999-12-31") == ("1999", "12", "31")


def test_invalid_day():
    with raises(SystemExit) as exc:
        check_date_format("2022-12-32")
    assert exc.value.code == "Invalid date"


def test_invalid_month():
    with raises(SystemExit) as exc:
        check_date_format("2022-13-31")
    assert exc.value.code == "Invalid date"


def test_invalid_date_format():
    with raises(SystemExit) as exc:
        check_date_format("2022/12/32")
    assert exc.value.code == "Invalid date"


def test_invalid_date_format2():
    with raises(SystemExit) as exc:
        check_date_format("Jan 1, 2022")
    assert exc.value.code == "Invalid date"
