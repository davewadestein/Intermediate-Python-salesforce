class AccessCounter:
    '''Maintain a value and keep track of number of times the
       value is changed.
    '''

    def __init__(self, val):
        super().__setattr__('counter', 0)
        super().__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super().__setattr__('counter', self.counter + 1)
        if name != 'counter':
            super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            self.counter += 1
        super().__delattr__(name)
