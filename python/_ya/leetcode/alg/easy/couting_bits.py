
class Solution:
    def countBits(self, n):
        memo = [0] * (n+1)
        for i in range(1, n + 1):
            memo[i] = memo[i >> 1] + i % 2
        return memo

if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/counting-bits/
        Дано: Дано целое положительное число
        Необходимо: Вернуть массив длины n + 1, в котором каждое число - кол-во 1 в битовом представлении
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    n = 5
    print(solution.countBits(n))
