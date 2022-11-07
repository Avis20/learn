class Solution:
    # Основание системы
    system_found = 10

    def is_digit_permutation(self, x: int, y: int) -> bool:
        digits_x = self.digits(x)
        digits_y = self.digits(y)
        return digits_x == digits_y

    def digits(self, num: int) -> dict:
        result = {}
        while num > 0:
            digit = num % self.system_found
            if digit not in result:
                result[digit] = 0
            result[digit] += 1
            num //= self.system_found
        return result


if __name__ == "__main__":
    """
    Ссылка:
    Дано: 2 числа X и Y, без ведущих нулей
    Необходимо: проверить можно ли получить первое из второго перестановкой цифр
    Примечание: Нужно чтобы числа были без ведущих нулей, чтобы можно было достать цифры через: dig = x % 10; x //= 10
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    num1 = 2021
    num2 = 1202
    print(solution.is_digit_permutation(num1, num2))
