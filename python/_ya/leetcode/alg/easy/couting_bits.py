
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):

            count = 0
            while i:
                # Прибавляем последний бит в двоичном числе
                count += i & 1
                # Сдвигаем на 1 символ вправа
                i >>= 1
            result.append(count)

        return result

if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/counting-bits/
        Дано: Дано целое положительное число
        Необходимо: Вернуть массив длины n + 1, в котором каждое число - кол-во 1 в битовом представлении
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    n = 5
    print(solution.countBits(n))
