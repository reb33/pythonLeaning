from multiprocessing import Process, freeze_support
import multiprocessing
from time import sleep


def f(name):
    sleep(1)
    print ("hello, "+str(name))


def main():
    p = Process(target=f, args=("World",))
    p.start()
    p.join()

if __name__ == '__main__':
    freeze_support()
    main()

# multiprocessing.Queue
# multiprocessing.Pipe()
# классы для обмена данными в мультипроцессовом приложении
