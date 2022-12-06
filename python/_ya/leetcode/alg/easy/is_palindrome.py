class Solution:
    def isPalindrome(self, s: str):

        left, right = 0, len(s) - 1

        while left <= right:

            # Если слева не буква или число - пропуск
            if not s[left].isalnum():
                left += 1
                continue

            # Если справа - пропуск
            if not s[right].isalnum():
                right -= 1
                continue

            print(s[left], s[right])
            # Если символы разные - значит не палиндром
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isPalindrome2(self, s: str):

        # Оставим в строке только буквы и цифры
        r = [c.lower() for c in s if c.isalpha() or c.isalnum()]

        n = len(r)
        # 1-я подстрока = с начала строки строго до середины
        s1 = r[: n // 2]
        # 2-я подстрока = с середины (-1 серединный символ), до конца строки
        # + reverse подстроки
        s2 = r[(n + 1) // 2 : n][::-1]
        return s1 == s2


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/valid-palindrome/
    Дано: Дана строка из букв, пробелов, спец символов
    Необходимо: Определить является ли строка палиндромом
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    # s = "0P"
    print(solution.isPalindrome(s))
