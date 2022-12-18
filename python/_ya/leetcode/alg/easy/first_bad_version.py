bad = 4


def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            print(f"right={right}; left={left}; mid={mid}")

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left





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
    n = 7
    print(solution.firstBadVersion(n))
