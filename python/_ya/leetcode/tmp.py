

class Solution:
    def findDisappearedNumbers(self, nums: list[int]):
        n = len(nums)
        i = 0
        while i < len(nums):
            corr_pos = nums[i] - 1
            if nums[i] != nums[corr_pos]:
                nums[i], nums[corr_pos] = nums[corr_pos], nums[i]
            else:
                i += 1

        result = []
        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result


    def findDisappearedNumbers2(self, nums: list[int]):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            num = nums[left]
            if num != left + 1:
                index = num - 1
                if nums[left] != nums[index]:
                    nums[left], nums[index] = nums[index], nums[left]
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            else:
                left += 1
        
        result = []
        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result


s = Solution()
nums = [4,3,2,7,8,2,3,1]
# nums = [1,1]
print(s.findDisappearedNumbers(nums))