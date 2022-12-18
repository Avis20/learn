class Solution:
    def reverseWords(self, s: str):
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)


if __name__ == "__main__":
    """
    Ссылка:
    Дано:
    Необходимо:
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    s = "Hello World"
    # s = "Let's take LeetCode contest"
    print(solution.reverseWords(s))
