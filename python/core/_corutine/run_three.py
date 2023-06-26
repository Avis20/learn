


def add(x, y):
    return x + y


def main():
    result = yield add(1, 2)
    print(result)
    yield



if __name__ == '__main__':
    print(next(main()))
