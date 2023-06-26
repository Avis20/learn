from typing import Optional, List
from multiprocessing import Pool, Process

from random import randint
from hashlib import sha256
from time import sleep
from datetime import datetime


def loads_words(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def hash_word(word: str, sleep_time=1) -> str:
    print(f"sleep_time = {sleep_time}")
    # print(word, sleep_time)
    hash_object = sha256()
    sleep(sleep_time)
    hash_object.update(word.encode("utf-8"))
    return hash_object.hexdigest()


def main_loop():
    # word_path = "/usr/share/dict/words"
    word_path = "./word_hashes.py"
    words = loads_words(word_path)
    start = datetime.now()
    print(f"Load {len(words)} from {word_path}. start={start}")

    words_with_sleep = []
    for word in words:
        sleep_time = randint(0, 5)
        words_with_sleep.append((word, sleep_time))

    while 1:
        sleep(2)
        print("main_loop", 1)
        hashed_words = {}
        with Pool(5) as pool:
            hashed_words = pool.starmap(hash_word, words_with_sleep)

        end = datetime.now()
        print(f"Done, with {len(hashed_words)} hashes. end={end}; diff={end - start}")


if __name__ == "__main__":
    # print()
    daemon_process = Process(target=main_loop)
    daemon_process.start()
