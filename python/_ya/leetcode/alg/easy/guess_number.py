
pick = 6
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            print(f"right={right}; left={left}; mid={mid}")

            answer = guess(mid)
            if answer == 0:
                return mid

            if answer == -1:
                right = mid
            else:
                left = mid


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
    n = 10
    print(solution.guessNumber(n))
