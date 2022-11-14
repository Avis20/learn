
class Solution:
    def climbStairs(self, n):
        if n in {0, 1}:
            return n
        
        n1 = 1
        n2 = 2
        for i in range(3, n + 1):
            n1, n2 = n2, n1 + n2
        
        return n2


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
    for i in [0, 1,2,3,4,5,6,7,8,9,10]:
        print(f"i = {i}; r={solution.climbStairs(i)}")
