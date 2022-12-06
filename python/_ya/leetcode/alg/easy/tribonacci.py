class Solution:
    def tribonacci(self, n: int):

        dp = [0, 1, 1]

        if n < 3:
            return dp[n]

        for i in range(3, n + 1):
            num = dp[i - 3] + dp[i - 2] + dp[i - 1]
            print(num)
            dp.append(num)
        print(dp)
        return dp[-1]


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/n-th-tribonacci-number/
    Дано: Дано число
    Необходимо: Найти
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    n = 5
    print(solution.tribonacci(n))
