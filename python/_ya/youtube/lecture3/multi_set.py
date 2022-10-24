class CustomSet:
    def __init__(self):
        # Фиксированный размер N мерного массива
        self.set_size = 10
        # создаем матрицу N на N
        self.custom_set = [[] for _ in range(self.set_size)]

    def __repr__(self):
        # цикл в цикле, эквивалентен коду
        # res = []
        # for xlist in self.custom_set:
        #     for number in xlist:
        #         res.append(str(number))
        # return ", ".join(res)
        return ", ".join(str(i) for j in self.custom_set for i in j)

    def add(self, x: int) -> None:
        hash_func = self._get_hash_func(x)
        print(f"->>> new number '{x}'; hash_func = {hash_func}")
        # Добавляем новый эл. в список
        if not self.isexist(x):
            self.custom_set[hash_func].append(x)

    def _get_hash_func(self, x):
        # вычисляем хеш функцию
        return x % self.set_size

    def isexist(self, x: int):
        hash_func = self._get_hash_func(x)
        for num in self.custom_set[hash_func]:
            if num == x:
                return True
        return False

    def delete(self, x: int):
        xlist = self.custom_set[self._get_hash_func(x)]
        for index in range(len(xlist)):
            # Если в списке есть искомый эл. 
            if xlist[index] == x:
                # Заменяем его на последний и удаляем последний через pop
                xlist[index] = xlist[-1]
                xlist.pop()
                return


if __name__ == "__main__":
    """
    Ссылка:
    Дано:
    Необходимо:
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    custom_set = CustomSet()
    print("custom_set =", custom_set)
    custom_set.add(3)
    custom_set.add(87)
    custom_set.add(17)
    print(f"10 is exists?", custom_set.isexist(10))
    print(f"100 is exists?", custom_set.isexist(100))
    custom_set.add(100)
    custom_set.add(100)
    custom_set.add(100)
    print(f"100 is exists?", custom_set.isexist(100))
    custom_set.delete(10)
    custom_set.delete(100)
    print("custom_set =", custom_set)
    custom_set.delete(87)
    print("custom_set =", custom_set)
    custom_set.delete(17)
    custom_set.delete(3)
    print("custom_set =", custom_set)
