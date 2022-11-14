

class Solution:
    def containsDuplicate(self, nums):
        sorted_nums = sorted(nums)
        is_same = False
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                is_same = True
        return is_same


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/contains-duplicate/
    Дано: Дан целочисленный массив чисел
    Необходимо:
        1) Вернуть true если хотя бы одно значение встречается дважды
        2) Вернуть false если все эл. различны
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.containsDuplicate(nums))
