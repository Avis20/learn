
from random import randint
from time import time, sleep

import multiprocessing as mp


def worker():
    sleep_time = randint(10, 20)
    print('sleep_time', sleep_time)
    sleep(sleep_time)


def main_loop():
    queue = mp.Queue()
    while True:
        processes = [mp.Process(target=worker) for _ in range(4)]

        start = time()
        
        for p in processes:
            p.start()
            p.join()

        end = time() - start
        print(f"diff = {end}")

        for p in processes:
            print(p.pid, p.is_alive())

        sleep(10)


if __name__ == '__main__':
    main_loop()


