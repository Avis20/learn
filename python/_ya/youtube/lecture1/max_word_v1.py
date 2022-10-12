
from sys import argv

class Solution:
    def max_word(self, string: str):
        # символ который максимально часто встречается
        answer = ""
        # сколько раз встречается максимальный символ
        answer_count = 0
        for i in range(len(string)):
            # В начале цикла буква string[i] встречалась 0 раз
            work_count = 0
            for j in range(len(string)):
                # Если мы встретили такой же символ что и во внешнем цикле
                if string[i] == string[j]:
                    # прибавим к рабочей переменной +1
                    work_count += 1
            # Если рабочая переменная больше максимального, запишем максимальный и сохраним букву
            if work_count > answer_count:
                answer = string[i]
                answer_count = work_count
        print(f"'{answer}', count={answer_count}")


if __name__ == "__main__":
    """
        Ссылка: https://youtu.be/QLhqYNsPIVo
        Дано: Дана строка (в кодировке UTF-8)
        Необходимо: Найти самый часто встречающийся в ней символ.
        Примечание: Если несколько символов встречается одинаково часто, то можно вывести любой
        Решение: Переберем все позиции и для каждой позиции в строке еще раз переберем все позиции и в случае совпадения прибавим к  счетчику единицу. Найдем максимальное значение счетчика
        Сложность алгоритма = O(N^2) т.к. используется вложенный цикл
    """
    solution = Solution()
    string = "ababab"
    with open(argv[1], "r", encoding="utf-8", errors="replace") as file:
        string = file.read()
    print(solution.max_word(string))
    # >>> ' ', count=369
