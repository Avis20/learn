

class Solution:
    def is_leflood(self, block_list: list[int]):
        # Определим индекс вершины и от него посчитаем сколько заполнено слева, а сколько справа
        # Если вершин будет несколько, то ничего страшного, найдем первую из них
        maxpos = 0
        for index in range(len(block_list)):
            if block_list[index] > block_list[maxpos]:
                maxpos = index
        print("maxpos", maxpos)
        answer = 0
        new_max = 0

        # Пройдем слева до вершины (от 0 до maxpos) 
        for index in range(maxpos):
            if block_list[index] > new_max:
                new_max = block_list[index]
            answer += new_max - block_list[index]
        print("answer left", answer)
        new_max = 0
        for index in range(len(block_list) - 1, maxpos, -1):
            if block_list[index] > new_max:
                new_max = block_list[index]
            answer += new_max - block_list[index]
        print("answer", answer)


if __name__ == "__main__":
    """
    Ссылка: https://youtu.be/SKwB41FrGgU
    Дано: Игра PitCraft происходит в двумерном мире, который состоит из блоков размером 1 на 1 метр. Остров игрока представляет собой набор столбцов различной высоты, состоящих из блоков камня и окруженный морем. Над островом прошел сильный дождь, который заполнил водой все низины, а не поместившаяся в них вода стекла в море, не увеличив его уровень
    Необходимо: По ландшафту острова определите, сколько блоков воды осталось после дождя в низинах на острове.
    """
    solution = Solution()
    block_list = [3, 1, 4, 3, 5, 1, 1, 3, 1]
    print(solution.is_leflood(block_list))
