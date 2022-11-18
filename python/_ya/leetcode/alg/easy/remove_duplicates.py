

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(f"org {nums}")

        # Начинаем с 1-го эл.
        j = 0
        for i in range(len(nums)):
            # Ищем эл. больше текущего
            # Текущий эл. - сразу пас
            if nums[i] > nums[j]:
                # Как только нашли больше текущего - переместили указатель
                j += 1
                # и заменили след. эл. большим предыдущего
                nums[j] = nums[i]

        print(f"res {nums}; {j}")
        return j

if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        Дано: Дан массив целых чисел с дублирующими значениями
        Необходимо: Убрать дубли на месте
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    nums = [0,0,0,0,0,0,1,1]
    nums = [1,1,2]
    nums = [1,1]
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))
