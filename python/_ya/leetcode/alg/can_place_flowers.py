

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        nums = flowerbed

        for i in range(len(nums)):
            prev_val = nums[i - 1] if i - 1 >= 0 else 0
            next_val = nums[i + 1] if i + 1 < len(nums) else 0
            print(prev_val, nums[i], next_val)
            if prev_val == nums[i] == next_val == 0:
                nums[i] = 1
                n -= 1
        print(nums)

        return True if n <= 0 else False


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
    flower, n = [1, 0, 0, 0, 1], 1 # t
    flower, n = [1,0,0,0,1], 2 # f
    flower, n = [1,0,0,0,0,1], 2 # f
    flower, n = [0,0,1,0,1], 1 # t
    flower, n = [1,0,0,0,1,0,0], 2
    flower, n = [0, 0, 1, 0, 0], 1  # t
    print(solution.canPlaceFlowers(flower, n))
