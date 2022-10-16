

class Solution:
    def findx(self, nums: list[int], target: int):
        answer = -1
        for i in range(len(nums)):
            if nums[i] == target:
                answer = i
        return answer


if __name__ == "__main__":
    """
        Ссылка: https://youtu.be/SKwB41FrGgU
        Дано: Дана последовательность чисел диной N
        Необходимо: Найти первое (правое) вхождение положительного числа x в нее или вывести -1, если число x не встречалось
        Решение: Сначала положим в ответ -1, затем будем перебирать все эл. Если текущий эл. равен x, запишем в ответ текущую позицию
        Сложность алгоритма: O(N)
    """
    solution = Solution()
    nums = [1,2,1,2,3]
    print(solution.findx(nums, 2))
