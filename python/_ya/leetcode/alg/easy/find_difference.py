
from collections import Counter


class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        return list((Counter(t) - Counter(s)).elements())[0]

    def findTheDifference2(self, s: str, t: str) -> str:
        # Запишем искомую строку без лишней буквы + сделаем сортировку чтобы точно ее найти
        search_string = "".join(sorted(s))
        buf = {}

        # Сделаем сортировку букв ранее перемешаной строки
        st = sorted(t)
        for del_pos in range(len(st)):
            # Удалим букву из последовательности и запишем в хеш
            # start = от начала строки, то i-го эл.
            # для i=0, st[0:0]=[], для i=1, st[0:1]=['a'] и т.п.
            start = st[:del_pos]
            # end будет от след. символа, до конца строки
            # для i=0, st[1:n]=['b', 'c', 'd'], для i=1, st[2:n]=['c', 'd'] и т.п.
            end = st[del_pos + 1 :]
            key = "".join(start + end)
            # запишев ключи=слова без выколотой буквы
            buf[key] = st[del_pos]

        # вернем выколотую букву
        return buf[search_string]


if __name__ == "__main__":
    """
    Ссылка:
    Дано:
    Необходимо:
    Примечание:
    Решение:
    Сложность алгоритма: O(N + M)
    """
    solution = Solution()
    s, t = "a", "aa"
    s, t = "cdab", "abecd"
    s, t = "abd", "dbae"
    print(solution.findTheDifference(s, t))
