

class Solution:
    def findMaxAverage(self, nums, k):
        
        sum_nums = sum(nums[0:k])
        max_avg = sum_nums / k

        for i in range(k, len(nums)):
            sum_nums -= nums[i - k]
            sum_nums += nums[i]
            max_avg = max(max_avg, sum_nums / k)
        return max_avg
        
        # left, right = 0, k
        # while len(nums) > right:
        #     # Уберем левый эл. и прибавим правый, чтобы посчитать новый максимум
        #     sum_nums = sum_nums - nums[left] + nums[right]
        #     max_avg = max(sum_nums / k, max_avg)
        #     left += 1
        #     right += 1
        # return max_avg


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/maximum-average-subarray-i/description/
    Дано: Дан массив целых чисел и число k
    Необходимо: Найти подмассив размера k у которого максимальное среднее значение
    Пример: ([1, 12, -5, -6, 50, 3], 4)  = [12 + -5 + -6 + 50] / 4 = 51 / 4 = 12.75
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [8, -19, 5, -4, 20] # 21
    nums = ([-1], 1)  # -1
    nums = ([6], 1)
    nums = ( [ 8860, -853, 6534, 4477, -4589, 8646, -6155, -5577, -1656, -5779, -2619, -8604, -1358, -8009, 4983, 7063, 3104, -1560, 4080, 2763, 5616, -2375, 2848, 1394, -7173, -5225, -8244, -809, 8025, -4072, -4391, -9579, 1407, 6700, 2421, -6685, 5481, -1732, -8892, -6645, 3077, 3287, -4149, 8701, -4393, -9070, -1777, 2237, -3253, -506, -4931, -7366, -8132, 5406, -6300, -275, -1908, 67, 3569, 1433, -7262, -437, 8303, 4498, -379, 3054, -6285, 4203, 6908, 4433, 3077, 2288, 9733, -8067, 3007, 9725, 9669, 1362, -2561, -4225, 5442, -9006, -429, 160, -9234, -4444, 3586, -5711, -9506, -79, -4418, -4348, -5891, ], 93, )  # -594.58065
    nums = ([4, 0, 4, 3, 3], 5)  # 2.8
    nums = ([1, 12, -5, -6, 50, 3], 4) # 12.75
    print(solution.findMaxAverage(*nums))
