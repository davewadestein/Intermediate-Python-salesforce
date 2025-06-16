"""A bunch of shared functions for the doohickey team."""

FOO_BAR = "foo...bar"


def func1():
    """func1"""
    return None


def func2(x):
    """func2"""
    return x + 1


def func3(x, y, z):
    """func3"""
    return x + y + z


# "unit tests" – not great, but better than nothing

if __name__ == '__main__':
    assert func1() is None
    assert func2(1) == 2
    assert func3(1, 2, 3) == 6
