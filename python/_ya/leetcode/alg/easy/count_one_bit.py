

class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in f"{n:0b}" if int(i) > 0])
        


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
    n = 11
    print(solution.hammingWeight(n))
