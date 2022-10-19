

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        if low % 2 == 0 and high % 2 == 0:
            count = (high - low) // 2
        else:
            count = (high - low) // 2 + 1
        return count


    def countOdds2(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        return len(range(low, high + 1, 2))

if __name__ == "__main__":
    """
        Ссылка:
        Дано: Два числа low и high
        Необходимо: Вернуть кол-во нечетных чисел от low до high (включительно)
        Примечание:
        Решение: 
        Сложность алгоритма: O(N)
    """
    solution = Solution()
    print(solution.countOdds(3, 7))
    print(solution.countOdds(8, 10))
    print(solution.countOdds2(800445804, 97943054000000000003))
