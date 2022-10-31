
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a + b > c:
                return a + b + c
        return 0

if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/largest-perimeter-triangle/description/
        Дано: Дан массив целых чисел
        Необходимо: Вернуть длину максимального периметра треугольника с не пустой площадью.
        Примечание: Если площадь пустая вернуть 0
        Решение: 
        Сложность алгоритма: O(N log N)
    """
    solution = Solution()
    nums = [3, 4, 15, 2, 9, 4]
    nums = [1, 2, 3, 4, 5]
    nums = [2, 1, 2]
    nums = [3, 2, 3, 4]
    print(solution.largestPerimeter(nums))
    # print(len(nums))
