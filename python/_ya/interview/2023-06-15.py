from typing import Literal

class Solution:
    def func(self, row: list[Literal[1, 0]]):
        count = 0
        max = 0
        prev = None
        for i in row:
            if i == 0:
                if prev and prev == 1:
                    count += 2
                else:
                    count += 1
            else:
                if max < count:
                    max = count
                count = 0
            prev = i
        if max < count:
            max = count
        return max // 2

if __name__ == "__main__":
    """
    Дан ряд кинотеатра

    """
    solution = Solution()
    n = [1, 1, 0, 0, 0, 1, 1] # 2
    n = [1, 1, 0] # 2
    print(solution.func(n))




