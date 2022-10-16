class Solution:
    def find_two_max(self, nums: list[int]):
        max1 = max(nums[0], nums[1])
        max2 = min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max2 = nums[i]
        return max1, max2


if __name__ == "__main__":
    """
    Ссылка: https://youtu.be/SKwB41FrGgU
    Дано: Дана последовательность чисел диной N (N > 1)
    Необходимо: Найти максимальное число в последовательности и второе по величине число (такое, которое будет максимальным, если вычеркнуть из одно максимальное число из последовательности)
    Решение:
        Заведем 2 переменные для первого и второго максимума - max, max2.
        Возьмем первые два числа из последовательности и запишем большее в max, а меньшее в max2.
        Если очередное число больше max, то запишем в max2 значение max, а в max - новый максимум.
        Если число только больше max2, запишем в max2
    Сложность алгоритма: O(N)
    """
    solution = Solution()
    nums = [1, 2, 1, 2, 3]
    print(solution.find_two_max(nums))
