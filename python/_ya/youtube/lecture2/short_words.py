from sys import argv


class Solution:
    def short_words(self, string: list[str]):
        min_len = len(string[0])
        for index in range(1, len(string)):
            word_len = len(string[index])
            if word_len < min_len and word_len > 0:
                min_len = word_len
        answer = []
        for word in string:
            if len(word) == min_len:
                answer.append(word)
        return " ".join(answer)


if __name__ == "__main__":
    """
    Дано: Дана последовательность слов
    Необходимо: Найти все самые короткие слова через пробел.
    Решение:
    Сложность алгоритма: O(2N)
    """
    solution = Solution()
    s = ""
    with open(argv[1], "r", encoding="utf-8", errors="replace") as file:
        line = file.read()
        s += line.replace("\n", " ")
    print(solution.short_words(s.split(" ")))
