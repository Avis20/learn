
class Solution:
    def findDisappearedNumbers(self, nums):
        i = 0
        while i < len(nums):
            print(nums)
            num = nums[i]
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
        print(nums)



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
    nums = [1,1]
    nums = [3,1,1]
    print(solution.findDisappearedNumbers(nums))
