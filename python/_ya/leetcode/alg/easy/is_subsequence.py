
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j = 0

        for c in t:
            if j < len(s) and s[j] == c:
                j += 1

        return j == len(s)
            



if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/is-subsequence/
        Дано:
        Необходимо:
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    s1 = "acb"
    s2 = "ahbgdc"
    print(solution.isSubsequence(s1, s2))

