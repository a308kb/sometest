import pytest


def test_float_sign():
    assert abs(5.2 * -1) == 5.2


@pytest.mark.parametrize("x,y", [(5.2, -7.3), (8.4, 14.6)])
def test_float_mult(x, y):
    assert (x * y) == (y * x)


def test_str_concat():
    assert "a" + "b" == "ab"


def test_str_len():
    assert len("ab") == 2


def test_set_in():
    assert '2' in {'4', '7', '2'}


def test_set_eq():
    assert {2, 7, 5} == {7, 5, 2}


def test_negative():
    try:
        assert "ab"[3] == ""
    except IndexError:
        pass
