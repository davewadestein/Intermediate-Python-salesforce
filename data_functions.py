"""Gazornin functions needed by the data team."""


def intify(num_string):
    """Return the integer value of a string.

    Returns None if the string can't be "int-ified".
    """
    try:
        return int(num_string)
    except ValueError:
        return None
    

def convert_strings_to_ints(list_of_strings):
    """Return a list of ints from each converted string."""

    numeric_vals = []
    
    for string in list_of_strings:
        try:
            numeric_vals.append(int(string))
        except ValueError:
            numeric_vals.append(-1) # if conversion fails, substitute a -1
    
    return numeric_vals


def invert_a_dict(d):
    """Invert a dictionary and return the inverted dict.
    
    Won't work if any values in the dictionary are mutable.
    """
    inverted_d = {} # create an empty dict

    for key in d: # for each key in the dict passed to us
        inverted_d[d[key]] = key

    return inverted_d

    # we could do that with a dict comprehension

    inverted_d = { d[key]: key for key in d }


if __name__ == '__main__':
    assert intify('a') is None
    assert intify('123') == 123
    assert convert_strings_to_ints([]) == []
    assert convert_strings_to_ints(['1', '2', '3x']) == [1, 2, -1]
    assert invert_a_dict({}) == {}
    assert invert_a_dict({ 'one': 1 }) == { 1: 'one' }
    try:
        # should throw a TypeError
        invert_a_dict({ 'one': [] })
        raise Exception('Oops, inverting dict did not throw TypeError')
    except TypeError:
        pass
    print('all tests passed')