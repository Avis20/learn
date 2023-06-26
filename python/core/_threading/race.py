
from threading import Thread, Lock

counter = 0

lock = Lock()

def increment():
    global counter
    for i in range(2000000):
        with lock:
            counter += 1


if __name__ == '__main__':
    for i in range(2):
        thread1 = Thread(target=increment)
        thread1.start()

        thread2 = Thread(target=increment)
        thread2.start()
        thread1.join()
        thread2.join()

    print(counter)
