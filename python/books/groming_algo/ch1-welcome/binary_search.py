class Solution:
    def binary_search(self, nums: list, target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            # (0 + 10) // 2 = 10 // 2 = 5
            # (6 + 10) // 2 = 16 // 2 = 8
            # (6 + 7) // 2 = 13 // 2 = 6
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


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
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(solution.binary_search(nums, 6))
