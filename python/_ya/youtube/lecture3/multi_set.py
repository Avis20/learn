from turtle import pd


class CustomSet:
    def __init__(self):
        self.set_size = 10
        self.custom_set = [[] for _ in range(self.set_size)]

    def __repr__(self):
        return ", ".join(str(i) for j in self.custom_set for i in j)

    def add(self, n: int) -> None:
        pass


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
    print(custom_set)
    # custom_set.add(10)
    # print(custom_set)
