import os
from time import sleep
from multiprocessing import Process


def printer(name):
    sleep(120)
    print("Привет", name)


if __name__ == "__main__":
    for i in range(5):
        proc = Process(target=printer, args=("Вася",))
        proc.start()
    print("hello")
    print("Главный пид", os.getpid())
    print("Дочерний процесс", proc.pid)
    proc.join()
