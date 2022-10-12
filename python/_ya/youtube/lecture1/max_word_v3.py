from sys import argv


class Solution:
    def max_word(self, string: str):
        # Заведем словарь для хранения пар: символ => сколько раз встречался в строке
        word_hash = {}
        # пройдем по всей строке
        for word in string:
            # если символа нет в словаре
            if word not in word_hash:
                # добавим в словарь и уст. кол-во раз сколько встречался = 0
                word_hash[word] = 0
            # т.к. мы точно знаем что символ в словаре есть, прибавим 1
            word_hash[word] += 1
        # найдем максимальный символ который встречается в словаре
        answer_count, answer = 0, ""
        for word in word_hash:
            if word_hash[word] > answer_count:
                answer = word
                answer_count = word_hash[word]
        print(f"word='{answer}'; count={answer_count}")


if __name__ == "__main__":
    """
    Ссылка: https://youtu.be/QLhqYNsPIVo
    Дано: Дана строка (в кодировке UTF-8)
    Необходимо: Найти самый часто встречающийся в ней символ.
    Примечание: Если несколько символов встречается одинаково часто, то можно вывести любой
    Решение: Заведем словарь, где ключом является символ, а значение - сколько раз он встретился. Если символ встретился впервые - создаем эл. словаря с ключом = символ, значение = 0. При новом появлении символа - прибавляем еще единицу
    Сложность алгоритма = O(N+K), где N - длина строки, K - кол-во символов в строке.
    т.к. K намного меньше N, сложность O(K) менее значим чем O(N)
    """
    solution = Solution()
    string = ""
    with open(argv[1], "r", encoding="utf-8", errors="replace") as file:
        line = file.read()
        string += line.replace("\n", "")
    print(solution.max_word(string))
    # >>> word='a'; count=8840897
