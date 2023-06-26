class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            c1 = s[i].lower()
            c2 = s[j].lower()
            if not c1.isalnum():
                i += 1
                continue
            if not c2.isalnum():
                j -= 1
                continue
            if c1 != c2:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    """
    
    """
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))
