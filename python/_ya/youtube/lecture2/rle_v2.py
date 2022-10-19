class NotValidStr(Exception):
    """Строка не валидная"""

    pass


class Solution:
    def rle_encode(self, s: str) -> str | None:
        if not self.validate(s):
            return
        answer = ""
        prev_word = ""
        count_word = 0
        for word in s:
            if word == prev_word:
                count_word += 1
                continue
            answer += self.pack(prev_word, count_word)
            count_word = 1
            prev_word = word
        if count_word:
            answer += self.pack(prev_word, count_word)
        return answer

    def pack(self, word: str, count: int) -> str:
        return f"{word}{count}" if count > 1 else word

    def rle_decode(self, s: str) -> str | None:
        if not self.validate(s, is_digit=True):
            return
        answer = ""
        prev_char = ""
        for char in s:
            if char.isdigit():
                answer += prev_char * (int(char) - 1)
            else:
                answer += char
            prev_char = char
        return answer

    def validate(self, s: str, is_digit=False):
        if s == "":
            return s
        try:
            if not s.isupper() or (not is_digit and not s.isalpha()):
                raise NotValidStr
        except NotValidStr:
            print(f"Строка '{s}' не валидная")
            return
        return s


if __name__ == "__main__":
    """
    Ссылка: https://youtu.be/SKwB41FrGgU
    Дано: Дана строка (возможно пустая), состоящая из букв A-Z: AAAAAABBBBCCCCXYZ
    Необходимо: Написать функцию RLE (Run Length Encoding), которая на входе принимает строку и возвращает сроку A6B4C4XYZ
    Пояснение: Если символ встречался 1 раз, он остается без изменений, если более 1 раза - к нему добавляется кол-во повторений
    Примечание: Если на вход подана не валидная строка - генерирует ошибку
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    s = ""
    res = solution.rle_encode(s)
    print(res)
    if res:
        print("res", res)
        print(solution.rle_decode(res))
