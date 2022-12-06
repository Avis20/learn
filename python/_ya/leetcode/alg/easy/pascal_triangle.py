
class Solution:
    def generate(self, numRows: int) -> list:
        # Вначале всего 1 уровень с 1 эл. 
        # Если numRows = 1, то сразу вернем первый уровень
        dp = [[1]]

        for level in range(1, numRows):
            # Что бы посчитать эл. для нового уровня, нужно пройтись по предыдущему
            prev_level = level - 1
            nums = []
            # Сразу добавим 1-й (а в конце последний) эл. = это будут единицы
            nums.append(dp[prev_level][0])

            # В середину добавим числа = суммы текущего и след. элемента
            for i in range(1, level):
                num = dp[prev_level][i-1] + dp[prev_level][i]
                nums.append(num)
            
            nums.append(dp[prev_level][-1])
            dp.append(nums)
        
        return dp


        



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
    n = 5
    print(solution.generate(n))
