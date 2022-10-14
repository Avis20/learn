from math import sqrt


class Solution:
    def func(self, a: int, b: int, c: int):
        if a == 0:
            if b != 0:
                x = -c / b
                return x
            if b == 0 and c == 0:
                return "inf"
        else:
            D = pow(b, 2) - 4 * a * c
            print("D =", D)
            if D == 0:
                x = -b / (2 * a)
                return x
            elif D > 0:
                x1 = (-b + sqrt(D)) / (2 * a)
                x2 = (-b - sqrt(D)) / (2 * a)
                if x2 > x1:
                    return (x1, x2)
                else:
                    return (x2, x1)


def test1():
    solution = Solution()
    assert solution.func(1, -2, 0) == (0.0, 2.0)


def test2():
    solution = Solution()
    assert solution.func(1, 2, 1) == (-1)


def test3():
    solution = Solution()
    assert solution.func(1, 1, 1) == None


def test4():
    solution = Solution()
    assert solution.func(0, 1, 1) == -1


def test5():
    solution = Solution()
    assert solution.func(0, 0, 1) == None


def test6():
    solution = Solution()
    assert solution.func(0, 0, 0) == "inf"


def test7():
    solution = Solution()
    assert solution.func(-5, 4, 1) == (-0.2, 1.0)


if __name__ == "__main__":
    """
    Ссылка:
    Дано: Заданы 3 целых числа, a, b, c
    Необходимо: Найти все корни уравнения ax^2 + bx + c = 0 и вывести их в порядке возрастания
    """
