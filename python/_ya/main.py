class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        end = k
        total_sum = sum(nums[start:end])
        total_max = total_sum

        while len(nums) > end:
            total_sum -= nums[start]
            total_sum += nums[end]

            if total_sum > total_max:
                total_max = total_sum

            start += 1
            end += 1

        return total_max / k


s = Solution()
nums, k = [1, 12, -5, -6, 50, 3], 4
# nums, k = [4,0,4,3,3], 5
nums, k = [7, 4, 5, 8, 8, 3, 9, 8, 7, 6], 7
nums, k = [5], 1
print("TOTALLLL =", s.findMaxAverage(nums, k))
