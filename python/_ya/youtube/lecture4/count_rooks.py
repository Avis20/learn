
from collections import defaultdict

class Solution:
    def count_beating_rooks(self, rook_coords):
        rooks_in_row = defaultdict(int)
        rooks_in_col = defaultdict(int)
        for row, col in rook_coords:
            rooks_in_row[row] += 1
            rooks_in_col[col] += 1
        print(rooks_in_row)
        print(rooks_in_col)
        p = self.count_pairs(rooks_in_row) + self.count_pairs(rooks_in_col)
        print(p)

    def count_pairs(self, hash: dict):
        pairs = 0
        for key in hash:
            pairs += hash[key] - 1
        return pairs

if __name__ == "__main__":
    """
        Ссылка: https://youtu.be/Nb5mW1yWVSs
        Дано: На шахматной доске N x N находятся M ладьей (ладья бьет клетки по горизонтали и вертикали)
        Необходимо:
            Определить сколько пар ладей бьют друг друга. 
            Ладьи задаются парой чисел I и J, обозначающие координаты клетки 
        Примечание: 
        Решение: 
            1) Для каждой занятой горизонтали и вертикали будем хранить кол-во ладей на них.
            2) Кол-во ладей в горизонтали (вертикали) равно кол-ву ладей - 1.
            3) Суммируем это кол-во пар для всех горизонталей и вертикалей
        Сложность алгоритма: 
    """
    solution = Solution()
    coords = [[1, 1], [4, 4], [1, 4]]
    print(solution.count_beating_rooks(coords))
