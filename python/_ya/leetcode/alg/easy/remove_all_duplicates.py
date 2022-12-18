class Solution:
    def removeDuplicates(self, s: str):
        stack = []

        for c in s:
            # Если есть стек и последний эл. это текущий, то удалим его
            # Иначе - добавим
            if stack and stack[-1] == c:
                stack.pop(-1)
            else:
                stack.append(c)

        # Остаток и есть ответ
        return "".join(stack)


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
    s = "abbaca"
    s = "azxxzy"
    print(solution.removeDuplicates(s))
