
from collections import defaultdict

class Solution:
    def char_histogram(self, s: str):
        # Посчитаем кол-во букв в строке
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        
        # Найдем максимальный и отсортируем словарь по ключам
        max_level = max(char_dict.values())
        sort_chars = sorted(char_dict.keys())
        
        # Будем идти от самого высокого уровня (буква которая встречается чаще всего)
        # к минимальной (реже всего)
        for i in range(max_level, 0, -1):
            for char in sort_chars:
                if char_dict[char] >= i:
                    print("#", end="")
                else:
                    print(' ', end="")
            print()

        print("".join(sort_chars))
        


if __name__ == "__main__":
    """
        Ссылка: 
        Дано: Дана строка S
        Необходимо: Вывести гистограмму как в примере
        Примечание: Коды символов отсортированы
        Пример: S = Hello, world!

              #
              ##
        ##########
         !,Hdelorw

        Решение: 
        Сложность алгоритма: O(N^2)
    """
    solution = Solution()
    S = "Hello, world!"
    print(solution.char_histogram(S))
