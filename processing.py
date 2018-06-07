# from multiprocessing import Process
# import os

# def processMethod(p):
#     print('执行方法(%s)，id:%s' % (p, os.getpid()))

# if (__name__ == '__main__'):
#     p1 = Process(target=processMethod, args=('p1', ))
#     p2 = Process(target=processMethod, args=('p2', ))
#     print('start...')
#     p1.start()
#     p2.start()
#     # p1.join()
#     # p2.join()
#     print('end')

#---------------------------------------------------

# from multiprocessing import Process, Pool
# import os, time, random

# def m1(name):
#     s = time.time()
#     time.sleep(random.random() * 4)
#     e = time.time()
#     print('name:%s,id:%s,timspan:%0.2f' % (name, os.getpid(), e - s))

# def m2(name):
#     s = time.time()
#     time.sleep(random.random() * 4)
#     e = time.time()
#     print('name:%s,id:%s,timspan:%0.2d' % (name, os.getpid(), e - s))

# if (__name__ == '__main__'):
#     print('Parent ID:%s' % os.getpid())
#     p = Pool(8)
#     for i in range(8):
#         p.apply_async(m1, args=(i, ))
#     p.close()
#     p.join()
#     print('end')

#----------------------------------------------------------

# from multiprocessing import Process, Queue

# def Qin(q):
#     for x in range(7):
#         q.put(x)
#         print('in:', x)

# def Qout(q):
#     while True:
#         print(q.get(True))

# if (__name__ == '__main__'):
#     queuemsg = Queue()
#     p1 = Process(target=Qin, args=(queuemsg, ))
#     p2 = Process(target=Qout, args=(queuemsg, ))
#     p1.start()
#     p2.start()
#     p1.join()

#     p2.terminate()

# import threading, multiprocessing

# def loop(x):
#     while True:
#         x = x ^ 1

# for x in range(multiprocessing.cpu_count()):
#     t1 = threading.Thread(target=loop, args=(x, ))
#     t1.start()

# #ThreadLoacl 线程全局变量，每个线程访问互不干扰

# import threading

# thLoacl = threading.local()


# def printst():
#     stname = thLoacl.stname
#     print('Thread:%s,StName:%s' % (threading.current_thread().name, stname))


# def loop(stname):
#     thLoacl.stname = stname
#     printst()

# if (__name__ == '__main__'):
#     for i in range(10):
#         t = threading.Thread(target=loop, args=(i, ), name='线程' + str(i))
#         t.start()
