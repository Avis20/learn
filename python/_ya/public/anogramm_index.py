

class Solution:
    def anagram_index(self, s: str, p: str) -> list[int]:
        anagram = set()
        n = len(p)
        for i in range(n):
            start = p[i:]
            end = p[:i]
            anagram.add(start + end)
        print(anagram)

        answer = []
        for i in range(len(s)):
            word = s[i:i + n]
            if word in anagram:
                print(word)
                answer.append(i)
        return answer


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
    s, p = "abcba", "ab" # [0, 3]
    s, p = "abcba", "a" # [0, 3]
    s, p = "abcdefgbca", "abc" # [0, 3]
    print(solution.anagram_index(s, p))
