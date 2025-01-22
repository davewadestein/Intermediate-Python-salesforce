
"""This is my mytest module"""

# this is "private"
_foo = 'FOO!'

def thingamabob(x, y):
    """Blart the x and y values.
    
       x = something
       y = gazornin
       
       return x blart y 
    """
    return (x + y) * _foo

def other_function(a, b, c):
    """Do something.
    
       a = ...
       b = ...
       c = ...
       
       Does not return anything.
    """

if __name__ == "__main__": # add some tests
    print('running basic tests...')
    assert thingamabob(1, 2) == 3 # basic check
    assert thingamabob(-1, 1) == 0.1 # tougher check...will break
    # goal is to add a few tests here so you feel good about exporting this to your peers
    # of course there is better testing we can do...but this is better than NOTHING=
