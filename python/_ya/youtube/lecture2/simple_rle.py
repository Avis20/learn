

class Solution:
    def simple_rle(self, s: str):
        if not s:
            return ""
        last_sym = s[0]
        answer = []
        for i in range(1, len(s)):
            if last_sym != s[i]:
                answer.append(last_sym)
                last_sym = s[i]
        answer.append(last_sym)
        return "".join(answer)


if __name__ == "__main__":
    """
        Ссылка: 
        Дано:
            Дана строка (возможно пустая), состоящая из букв A-Z
            AAAAAAAAAAAABBBCCCAAAAA
        Необходимо: Написать функцию, которая на выводе даст строку вида: ABCA
        Примечание: 
        Решение: 
        Сложность алгоритма: 
    """
    solution = Solution()
    s = "AA"
    print(solution.simple_rle(s))
