

class NumArray:

    def __init__(self, nums):
        sums = []

        # Создадим заранее массив со всеми суммами пред. чисел включая это число
        counter = 0
        for i in range(len(nums)):
            counter += nums[i]
            sums.append(counter)
        
        self._sums = sums

    def sumRange(self, left, right):
        if left == 0:
            # Если нужна сумма от 0, то просто вернем подсчитанную сумму
            return self._sums[right]
        return self._sums[right] - self._sums[left-1]
        # return sum(self._nums[left:right+1])


if __name__ == "__main__":
    """
        Ссылка:
        Дано:
        Необходимо:
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(2, 5))
