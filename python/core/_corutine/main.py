
from typing import Generator

import math

def cash_return(deposit: int, percent: float, years: int) -> float:
    value = math.pow(1 + percent / 100, years)
    print("value", value)
    return round(deposit * value, 2)

def cash_return_coro(percent: float, years: int) -> Generator[float, int, None]:
    value = math.pow(1 + percent / 100, years)
    print("value", value)
    while True:
        try:
            deposit = (yield)
            yield round(deposit * value, 2)
        except GeneratorExit:
            print("Corutine end")
            raise

def coro():
    val = (yield)
    print(val)

if __name__ == '__main__':
    # cor = coro()
    # for i in cor:
    #     cor.send(1)
    #     cor.close()

    # print(cash_return(1_000_000, 7.2, 3))

    cor = cash_return_coro(5, 5)
    next(cor)
    values = [1000, 2000, 3000, 4000, 5000, 10000]
    for item in values:
        print(cor.send(item))
        # next(cor)
    # cor.close()

