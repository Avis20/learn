
from random import randint
from multiprocessing import Process, Pool


from time import sleep

pool = Pool()


def task():
    s = randint(0, 5)
    sleep(s)
    print("i am task", s)


def main_loop():
    while 1:
        sleep(2)
        print("main_loop", 1)
        with Pool(5) as pool:
            res = pool.apply(task)


if __name__ == "__main__":
    # print()
    daemon_process = Process(target=main_loop)
    daemon_process.start()
