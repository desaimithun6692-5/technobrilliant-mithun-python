from threading import Thread
from time import sleep


class Hi(Thread):

    def run(self):
        for i in range(500):
            print("Hi")
            sleep(1)


class Hello(Thread):

    def run(self):
        for i in range(500):
            print("hello")
            sleep(1)



t1 = Hi()
t2 = Hello()

t1.start()
t2.start()


print("bye")