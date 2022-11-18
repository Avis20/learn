

class Solution:
    def addDigits(self, num):

        while num >= 10:
            curr = num
            sum_num = 0
            while curr:
                curr, div = divmod(curr, 10)
                sum_num += div
            num = sum_num
        return num

    def addDigits2(self, num):
        
        res, div = divmod(num, 10)
        while res:
            div_sum = 0
            while num > 0:
                num, div = divmod(num, 10)
                div_sum += div
            num = div_sum
            res, div = divmod(num, 10)
            print(res, div)
        return div


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/add-digits/description/
        Дано: Дано число
        Необходимо: Вернуть последнее целое число при делении

        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    num = 38
    print(solution.addDigits(num))
