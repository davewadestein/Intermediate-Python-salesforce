"""A bunch of shared functions for the doohickey team."""

FOO_BAR = "foo...bar" # constant


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

# smoke tests

if __name__ == '__main__': # are we running this Python file or importing it?
    assert func1() is None
    assert func2(1) == 2
    assert func3(1, 2, 3) == 6
    assert func2(-1) == 0, "Joe reported this" # replicated the failure pointed out to you by your peer
    print('all tests passed')
