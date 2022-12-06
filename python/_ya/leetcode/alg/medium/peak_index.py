class Solution:
    def peakIndexInMountainArray(self, arr: list):

        left, right = 0, len(arr) - 1
        while left < right:
            mid = (right + left) // 2

            # Если текущий больше пред. и больше след. - значит это вершина
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid

            # Если след. больше текущего, значит мы на спуске и нужно идти вверх
            # Иначе - мы прошли вершину и нужно идти обратно
            if arr[mid + 1] > arr[mid]:
                left = mid
            else:
                right = mid


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/peak-index-in-a-mountain-array/
    Дано: Дан массив `arr` длинной >= 3
    Необходимо: Найти вершину в этом массиве. Вернуть индекс значение для которого
        * arr[0] < arr[i - 1] < arr[i]
        * arr[i] > arr[i + 1] > arr[i]
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    nums = [0, 1, 0]
    nums = [0, 1, 3, 2, 1]
    nums = [18, 29, 38, 59, 98, 100, 99, 98, 90]
    print("result", solution.peakIndexInMountainArray(nums))
