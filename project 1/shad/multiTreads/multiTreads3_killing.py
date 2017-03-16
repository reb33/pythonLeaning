from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self):
        super().__init__()
        self.killing = False

    def run(self):
        for i in range(5):
            if self.killing:
                break
            print(i)
            sleep(2)

    def kill(self):
        self.killing = True

t = MyThread()
t.start()
sleep(1)
t.kill()