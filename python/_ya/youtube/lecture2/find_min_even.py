class Solution:
    def find_min_even(self, nums: list[int]):
        find_min = False
        min_even = nums[0]
        for n in nums:
            if n % 2 == 0 and n < min_even:
                find_min = True
                min_even = n
        return min_even if find_min else -1
        


if __name__ == "__main__":
    """
    Ссылка: https://youtu.be/SKwB41FrGgU
    Дано: Дана последовательность чисел диной N
    Необходимо: Найти минимальное четное число в последовательности или вывести -1, если такого не существует
    Решение:
        
    Сложность алгоритма: O(N)
    """
    solution = Solution()
    nums = [1, 2, 1, 2, 3, 0]
    print(solution.find_min_even(nums))
