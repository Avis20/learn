class Solution:
    def find_max(self, nums: list[int]):
        answer = nums[0]
        for n in nums:
            if n > answer:
                answer = n
        return answer


if __name__ == "__main__":
    """
    Ссылка: https://youtu.be/SKwB41FrGgU
    Дано: Дана последовательность чисел диной N
    Необходимо: Найти максимальное число в последовательности
    Решение:
        Сначала положим в ответ последний эл, затем будем перебирать все эл.
        Если текущий эл. больше ответа - запишем в ответ текущий эл.
    Сложность алгоритма: O(N)
    """
    solution = Solution()
    nums = [1, 2, 1, 2, 3]
    print(solution.find_max(nums))
