
class Solution:
    def rle_encode(self, s: str) -> str:
        if not s:
            return ""
        last_sym = s[0]
        last_pos = 0
        answer = []
        for i in range(len(s)):
            if last_sym != s[i]:
                answer.append(self.pack(last_sym, i - last_pos))
                last_pos = i
                last_sym = s[i]
        answer.append(self.pack(s[last_pos], len(s) - last_pos))
        return "".join(answer)

    def pack(self, s: str, count: int):
        if count > 1:
            return s + str(count)
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
    s = "AAAAAABBBBCCCCXYZA"
    print(solution.rle_encode(s))
    