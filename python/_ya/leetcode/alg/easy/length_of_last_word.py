

class Solution:
    def lengthOfLastWord(self, s: str):
        # Уберем символы с начала и с конца
        s_without_spaces = s.strip()
        # Разобьем по пробелам
        s_list = s_without_spaces.split(" ")
        # Вернем длину последнего символа
        return len(s_list[-1])


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/length-of-last-word/
        Дано: Дана строка содержащая слова и пробелы
        Необходимо: вернуть длину символов последнего слова
        Примечание:
    """
    solution = Solution()
    s = "   the   moon    te"
    print(solution.lengthOfLastWord(s))
