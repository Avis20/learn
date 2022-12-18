
from rich import inspect

from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return bisect_left(nums, target)

    def searchInsert2(self, nums: list[int], target: int) -> int:

        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            print(f"left={left}; right={right}; mid={mid}")

            # Если нашли искомый эл. вернем индекс
            if nums[mid] == target:
                return mid

            # Если есть след. эл. после mid (mid + 1 > n), то
            # Если target больше текущего и меньше след. то встанет на место след.
            if mid + 1 < n and target > nums[mid] and target < nums[mid + 1]:
                return mid + 1

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # Если мы не нашли эл. и не нашли место куда бы он встал, то
        # Если эл. меньше первого, значит он должен встать в начало
        # Иначе если он больше последнего - встать в конец
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return n


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
    # nums, t = [1, 3, 5, 6], 5 # 2
    # nums, t = [1, 3, 5, 6], 2 # 1
    # nums, t = [1, 3, 5, 6], 7 # 4
    # nums, t = [1, 3, 5, 6], 0 # 0
    nums, t = [1, 3], 1  # 0
    # nums, t = [2, 5], 1 # 1

    print('\n\n')
    print(inspect(inspect))
    print('\n\n')

    print(solution.searchInsert(nums, t))
