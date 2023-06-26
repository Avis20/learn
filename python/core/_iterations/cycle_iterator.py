from typing import Any


# Итератор должен итерироваться по итерируемому объекту
# (list, tuple, set, range, Range2, и т. д.), и когда достигнет последнего элемента, начинать сначала.

class CyclicIterator:
    def __init__(self, items: Any):
        self.curr_index = -1
        self.last_index = len(items) - 1
        self.items = items

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index < self.last_index:
            self.curr_index += 1
        else:
            self.curr_index = 0
        return self.items[self.curr_index]

if __name__ == '__main__':
    _list = [1, 2, 3]
    _tuple = (1, 2, 3)
    _range = range(3)
    # print(_range[2])

    cyclic_iterator = CyclicIterator(_range)
    for i in cyclic_iterator:
        print(i) 