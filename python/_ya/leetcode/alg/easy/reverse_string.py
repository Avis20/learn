class Solution:
    def reverseString(self, s: list):

        left, right = 0, len(s) - 1

        while left < right:
            # swap
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/reverse-string/description/
    Дано:
    Необходимо:
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    s = list("hello")
    print(solution.reverseString(s))
