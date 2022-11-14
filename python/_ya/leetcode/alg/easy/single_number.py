
class Solution:
    def singleNumber(self, nums):
        mask = 0
        for num in nums:
            print(f"mask {mask:04b}; num {num}={num:04b}", )
            mask ^= num
        return mask



if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/single-number/
        Дано: Дан не пустой целочисленный массив, каждое число встречается дважды
        Необходимо: Найти эл. который встречается один раз
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    nums = [3,1,2,1,2,3,4]
    print(solution.singleNumber(nums))
