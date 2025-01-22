class ZanyInt(int):
    def __add__(self, other):
        sum = super().__add__(other)
        return sum + 0.25
