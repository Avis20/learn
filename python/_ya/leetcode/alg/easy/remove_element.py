from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while n > i:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/remove-element/
        Дано: Дана последовательность целых чисел nums, и целое число val
        Необходимо: Удалить все вхождения числа val из последовательности nums на месте.
        Примечание: Порядок nums при этом может измениться
        Решение: При встрече нужного эл. - заменяем его на последний и уменьшаем правую границу
        Сложность алгоритма: O(n)
    """
    solution = Solution()
    # my_list = [3,2,2,3]
    my_list = [0,1,2,2,3,0,4,2]
    print(solution.removeElement(my_list, 2))
    print("my_list", my_list)