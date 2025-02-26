def document_it(func):
    # below is a nested, or inner function
    def new_function(*args, **kwargs):
        print(f'Running function: {func.__name__}')
        print(f'Positional arguments: {args}')
        print(f'Keyword arguments: {kwargs}')
        # here we invoke the function passed in as an argument
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        return result
    
    # document_it() is returning a reference to the inner function
    return new_function


def time_it(func):
    # below is a nested, or inner function
    def inner(*args, **kwargs): # function that we are wrapping takes ONE argument
        import time
        start = time.time()
        # here we invoke the function passed in as an argument
        result = func(*args, **kwargs) # call function func, with arg arg, and return
        elapsed_time = time.time() - start
        print(f'{func.__name__} took {elapsed_time:.2f} seconds to run')
        return result
    
    # document_it() is returning a reference to the inner function
    return inner