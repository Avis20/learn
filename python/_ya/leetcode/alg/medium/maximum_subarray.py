class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            curr_sum = max(curr_sum + num, num)
            print(curr_sum)
            max_sum = max(max_sum, curr_sum)

        return max_sum



if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/maximum-subarray/
    Дано: Дан массив целых чисел
    Необходимо: Вернуть сумму максимального подмассива
    Пример:
        [-2,1,-3,4,-1,2,1,-5,4]
        Ответ = 6
        [4,-1,2,1] - максимальный подмассив
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2] # -2
    # nums = [8, -19, 5, -4, 20] # 21
    # nums = [1,2,-1,-2,2,1,-2,1] # 3
    # nums = [2,0,-3,2,1,0,1,-2]
    print(solution.maxSubArray(nums))
