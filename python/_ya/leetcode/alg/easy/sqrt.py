

class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2

            sq = mid * mid
            print(left, right, '=', mid, 'sq', sq)
            if sq == x:
                return mid

            if sq > x:
                right = mid - 1
            else:
                left = mid + 1

            print(left, right)
        return right


        


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
    x = 16
    print(solution.mySqrt(x))
