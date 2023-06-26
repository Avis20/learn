

numbers = [1, 2, 3]

def func():
    # for item in numbers:
    #     yield item
    yield from numbers


def simple_gen():
    yield 1
    yield 2
    return 3


def gen_range(stop_val: int):
    stop_val -= 1
    curr = -1
    while curr < stop_val:
        curr += 1
        yield curr

if __name__ == '__main__':
    # for i in gen_range(3):
    #     print(i)

    gen = simple_gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

    # for i in func():
    #     print(i)
