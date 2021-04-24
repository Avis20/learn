from functools import wraps


def trace(func):
    func.level = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(map(lambda k, v: f"{k}:{v:r}", kwargs.items()))
        func_args = list(filter(bool, (args_str, kwargs_str)))
        print('__' * func.level + f"-> {func.__name__}({', '.join(func_args)})")
        func.level += 1
        result = func(*args, **kwargs)
        func.level -= 1
        print('__' * func.level + f"<- {func.__name__}({', '.join(func_args)}) == {result}")
        return result

    return wrapper


@trace
def fib(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # print(fib.__name__)
    # print(fib.__module__)
    print(fib(3))
