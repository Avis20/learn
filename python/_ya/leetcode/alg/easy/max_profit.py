

class Solution:
    def maxProfit(self, prices):

        max_profit = 0
        current_min = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]

            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)

        return max_profit


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
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    print(solution.maxProfit(prices))
