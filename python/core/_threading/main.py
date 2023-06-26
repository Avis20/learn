import os
from time import sleep
from threading import Thread



def printer(name):
    sleep(100)
    print("Привет", name)



if __name__ == '__main__':
    for i in range(5):
        thread = Thread(target=printer, args=('Петя',))
        thread.start()
        # thread.join()
    print("Main process")
    print("Главный пид", os.getpid())
    print("Дочерний процесс", thread)
