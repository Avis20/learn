
class Solution:
    def moveZeroes(self, nums):
        print(f"org = {nums}")

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                print(f"{nums[i]}, {nums[j]}")
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                print(f"tmp = {nums}; {j}")

        print(f"res = {nums}")
        return nums



if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/move-zeroes/
        Дано: Дан целочисленный массив
        Необходимо: Перенести все 0 в конец массива сохранив порядок
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    nums = [0,0,1,0]
    nums = [1]
    nums = [0,1,0,3,12]
    print(solution.moveZeroes(nums))
