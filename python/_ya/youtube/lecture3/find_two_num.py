

class Solution:
    def func(self, nums: list[int], x: int) -> tuple:
        prev_nums = set()
        for num in nums:
            if x - num in prev_nums:
                return num, x - num
            prev_nums.add(num)
        return 0, 0



if __name__ == "__main__":
    """
        Ссылка: 
        Дано: Дана последовательность положительных чисел N и число X
        Необходимо: Найти 2 различных числа A и B таких что A + B = X, или вернуть пару 0, 0 если такой пары нет
        Примечание: 
        Решение: Создадим множество уже обработанных чисел. Если очередное число num, и num - x есть в множестве, то вернем num и num - x
        Сложность алгоритма: O(N)
    """
    solution = Solution()
    nums = [1, 3, 5, 7, 10]
    print(solution.func(nums, 8))
    nums2 = list(range(10))
    print(nums2)
    print(solution.func(nums2, 5))

    # >>> (1, 7)
    # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # >>> (0, 5)