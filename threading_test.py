import threading
import time
import random


def sum(v1, v2):
    s = random.randint(1,10)
    print(s)
    time.sleep(s)
    return print(v1+v2)


threading.Thread(target=sum, args=(1, 2)).start()
threading.Thread(target=sum, args=(2, 2)).start()
threading.Thread(target=sum, args=(3, 2)).start()

print("main-thread")
