



class Solution:
    def subtactProductAndSum(self, n: int) -> int:
        digits = []
        while n > 0:
            digit = n % 10
            digits.append(digit)
            n //= 10
        sum(digits) - map(x * x: lambda, digits)



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
    n = 234
    print(solution.subtactProductAndSum(n))
