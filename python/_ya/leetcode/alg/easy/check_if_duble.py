

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        
        buf = {}
        for num in arr:
            # Проверим num * 2 - что бы найти 
            # на num / 2 нужен чтобы найти уже прошедшие цифры
            # Например nums = [7,1,14,11]
            if num * 2 in buf or num / 2 in buf:
                return True
            # Добавим в буфер уже пройденных цифр
            buf[num] = 1
        
        return False

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
    nums = [10,2,5,3]
    nums = [3,1,7,11]
    nums = [7,1,14,11]
    print(solution.checkIfExist(nums))
