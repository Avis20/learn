
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        add = 1
        # Будем добавлять с конца массива, т.е. с единиц
        for index in range(len(digits) - 1, -1, -1):
            # Если нечего добавлять, то просто запишем число в ответ
            if not add:
                answer.append(digits[index])
                continue
            digits[index] += add
            if digits[index] == 10:
                # Если при добавлении получилось переполнение == 10
                # Добавим 0 в начало ответа
                answer.append(0)
                if index == 0:
                    # И если это последнее число, добавим 1
                    answer.append(1)
            else:
                # Иначе просто добавим число и будем просто добавлять след. числа
                answer.append(digits[index])
                add = 0
        answer.reverse()
        return answer


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/plus-one/
        Дано: Число представленное в виде массива digital
        Необходимо: Увеличить число на 1 и вернуть также в виде массива
        Примечание: 
        Решение: 
        Сложность алгоритма: O(N)
    """
    solution = Solution()
    digits = [9, 9, 8]
    print(solution.plusOne(digits))
