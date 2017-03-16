from threading import Thread
import time


class MyThread(Thread):
    def __init__(self):
        super().__init__()
        self.status = "starting..."

    def run(self):
        time.sleep(1)
        self.status = "done"

t = MyThread()
t.start()
print(t.status)
print(t.is_alive())
t.join()
print(t.status)
print(t.is_alive())