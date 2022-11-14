

class Solution:
    def missingNumber(self, nums):
        sorted_nums = sorted(nums)
        for i in range(len(nums) + 1):
            if not i in sorted_nums:
                return i


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/missing-number/
        Дано: Дан целочисленный список содержащий n различных чисел в диапазоне от [0, n]
        Необходимо: вернуть отсутствующее число
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(solution.missingNumber(nums))
