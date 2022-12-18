

class Solution:
    def isPowerOfFour(self, n) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfFour(n / 4)


if __name__ == "__main__":
    """
        Ссылка:
        Дано:
        Необходимо:
        Примечание:
        Решение:
        Сложность алгоритма:
    """
    solution = Solution()
    n = 16
    # n = 2147483648
    print(solution.isPowerOfFour(n))
