class RangeIter:
    def __init__(self, container):
        self.container = container

    def __next__(self):
        if self.container.curr < self.container.stop_val:
            self.container.curr += 1
            return self.container.curr
        raise StopIteration


class Range:
    def __init__(self, stop_val: int):
        self.curr = -1
        self.stop_val = stop_val - 1

    def __iter__(self):
        return RangeIter(self)


if __name__ == "__main__":
    _range = Range(5)
    for i in _range:
        print(i)
