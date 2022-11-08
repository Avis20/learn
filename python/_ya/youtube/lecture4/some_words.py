from collections import defaultdict


class Solution:
    def some_words_group(self, words):
        some_words = defaultdict(list)
        for word in words:
            key = "".join(sorted(word))
            some_words[key].append(word)
        result = []
        for val in some_words.values():
            result.append(val)
        return result


if __name__ == "__main__":
    """
    Ссылка:
    Дано: Список слов
    Необходимо: Сгруппировать слова по общим буквам
    Пример:
        input = ["eat", "tea", "tan"]
        output = [["eat", "tea"], ["tan"]]
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.some_words_group(words))
