class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def typing(string: str):
            stack = []

            for char in string:
                if char == '#':
                    if stack:
                        stack.pop(-1)
                else:
                    stack.append(char)
            
            return stack

        return typing(s) == typing(t)


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
    s, t = "ab#c", "ad#c"
    s, t = "ab##", "c#d#"
    s, t = "ab##", "c"
    s, t = "y#fo##f", "y#f#o##f"
    print(solution.backspaceCompare(s, t))
