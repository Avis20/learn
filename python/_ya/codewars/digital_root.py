

def digital_root(n: int):

    while n > 9:
        new_n = 0
        k = n
        while k:
            k, d = divmod(k, 10)
            new_n += d
        n = new_n
    return n


if __name__ == "__main__":
    """
        Ссылка:
        Дано:
        Необходимо:
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    n = 10
    # n = 942
    print(digital_root(n))
