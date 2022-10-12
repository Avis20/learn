
from sys import argv


class Solution:
    def max_word(self, string: str):
        # символ который максимально часто встречается
        answer = ""
        # сколько раз встречается максимальный символ
        answer_count = 0
        # цикл по уникальным символам строки
        for word in set(string):
            # В начале цикла буква word встречалась 0 раз
            work_count = 0
            for j in range(len(string)):
                # если встретили искомый символ
                if word == string[j]:
                    # прибавим к рабочей переменной +1
                    work_count += 1
            # Если рабочая переменная больше максимального, запишем максимальный и сохраним букву
            if work_count > answer_count:
                answer = word
                answer_count = work_count
        print(f"'{answer}', count={answer_count}")


if __name__ == "__main__":
    """
        Ссылка: https://youtu.be/QLhqYNsPIVo
        Дано: Дана строка (в кодировке UTF-8)
        Необходимо: Найти самый часто встречающийся в ней символ.
        Примечание: Если несколько символов встречается одинаково часто, то можно вывести любой
        Решение: Переберем все символы, встречающийся в строке, а затем переберем все позиции и в случае совпадения прибавим единицу. Найдем максимальное число счетчика
        Сложность алгоритма = O(N*K), где N - длина строки, K - кол-во символов в строке
    """
    solution = Solution()
    string = "abababa"
    with open(argv[1], "r", encoding="utf-8", errors="replace") as file:
        string = file.read()
    print(solution.max_word(string))
    # >>> ' ', count=369
