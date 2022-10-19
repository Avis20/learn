from sys import argv


class Solution:
    def short_words(self, string: list[str]):
        index_list = [0]
        min_len = len(string[0])
        for index in range(1, len(string)):
            word_len = len(string[index])
            if word_len < min_len and word_len > 0:
                min_len = word_len
                index_list = [index]
            elif word_len == min_len:
                index_list.append(index)
        answer = []
        for index in index_list:
            answer.append(string[index])
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
