
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True
        
        left, right = 1, num
        while right > left:

            mid = (left + right) // 2
            
            square = mid * mid
            if square == num:
                return True

            print(f"{mid}, {square}")
            if square > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False



if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/valid-perfect-square/description/
        Дано: Дано число
        Необходимо: Вернуть True если число 
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    num = 17
    print(solution.isPerfectSquare(num))
