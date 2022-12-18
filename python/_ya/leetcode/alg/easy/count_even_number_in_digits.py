class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count_even = 0

        for num in nums:

            count_digits = 0
            while num > 0:
                num //= 10
                count_digits += 1

            if count_digits % 2 == 0:
                count_even += 1

        return count_even


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
    nums = [12, 345, 2, 6, 7896]
    nums = [555, 901, 482, 1771]
    print(solution.findNumbers(nums))
