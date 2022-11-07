


class Solution:
    def sort_with_count(self, nums: list[int]) -> list[int]:
        max_val = max(nums)
        min_val = min(nums)
        count_val = (max_val - min_val + 1)
        counter = [0] * count_val
        for num in nums:
            # индекс эл. = эл. - мин. значение 
            # т.е. если список [1, 10], для 10 в новом массиве индекс будет 10 - 1 = 9
            index = num - min_val
            counter[index] += 1
        print(counter)
        new_pos = 0
        for val in range(min_val, count_val):
            for i in range(counter[val]):
                print("val =", val + min_val, "count exist: ", i)
                nums[new_pos] = val + min_val
                new_pos += 1
        return nums


if __name__ == "__main__":
    """
        Ссылка: 
        Дано: Массив целых чисел
        Необходимо: Отсортировать в порядке возрастания
        Примечание: 
        Решение: 
            1) Вычислим макс. и мин. Чтобы создать новый массив. Вычислим длину массива
            2) Создадим массив от мин. до макс. заполнив его нулями
            3) Для каждого числа во входном массиве прибавим +1
            4) Для каждого значения числа выведем значение 
        Сложность алгоритма: 
    """
    solution = Solution()
    nums = [4,3,1,4,5,6,4,3,10]
    print(solution.sort_with_count(nums))
