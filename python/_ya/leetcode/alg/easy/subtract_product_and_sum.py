



class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Создаем словарь из чисел и инвертируем его т.к. читаем с конца
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits.reverse()

        sum_digits = 0
        prod_digits = None
        for digit in digits:
            print(digit)
            sum_digits += digit
            # Если ранее не было числа - записываем число
            # Иначе умножаем
            prod_digits = prod_digits * digit if prod_digits is not None else digit
        print(sum_digits, prod_digits)
        if prod_digits is None:
            return 0
        return prod_digits - sum_digits 



if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
    Дано: Дано целое число
    Необходимо: Найти разницу между суммой и произведением цифр в числе
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    n = 0
    # 7 + 0 + 5 = 12
    # 7 * 0 * 5 = 
    print(solution.subtractProductAndSum(n))
