# test code for function mean

from mean import mean # import the code being tested
import pytest

def test_ints():
    num_list = [1, 2, 3, 4, 5]
    assert mean(num_list) == 3

def test_zero():
    num_list = [0, 2, 4, 6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

def test_double():
    num_list = [1, 2, 3, 4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp

def test_long(): # in Python 2, there was a long datatype
    big = 100_000_000
    obs = mean(range(1, big))
    exp = big/2.0
    assert obs == exp

def test_complex():
    # given that complex numbers are an unordered field
    # the arithmetic mean of complex numbers is meaningless
    num_list = [2 + 3j,  3 + 4j,  -32 - 2j]
    obs = mean(num_list)
    exp = -9+1.6666666666666667j
    assert obs == exp

def test_empty_list():
    with pytest.raises(ValueError):
        mean([])
