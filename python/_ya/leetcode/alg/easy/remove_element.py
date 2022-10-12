from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/remove-element/
    Дано: Дана последовательность целых чисел nums, и целое число val
    Необходимо: Удалить все вхождения числа val из последовательности nums на месте.
    Примечание:
    """
    solution = Solution()
    # my_list = [3,2,2,3]
    my_list = [0,1,2,2,3,0,4,2]
    print(solution.removeElement(my_list, 2))
    print("my_list", my_list)
