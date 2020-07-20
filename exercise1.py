from threading import Thread, Event, Lock

lock1 = Lock()
lock2 = Lock()
e1=Event()
e2=Event()


def number():
    e1.wait(0.0005)
    for i in range(1, 53, 2):
        # lock1.acquire()
        e1.wait(0.001)
        print(i, end=" ")
        print(i + 1, end=" ")
        # lock2.release()



def ABC():
    for i in range(65, 91):
        # lock2.acquire()
        e2.wait(0.001)
        print(chr(i), end=" ")
        # lock1.release()


t1 = Thread(target=number)
t2 = Thread(target=ABC)
# lock2.acquire()
t1.start()
t2.start()
