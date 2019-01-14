# Time    : 12/27/2018 9:53 AM
# Author  : Luzaofa

import time
import threading


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        apply(self.func, self.args)


class Demo(object):

    def __init__(self):
        self.mass = [i for i in range(10000)]

    def test(self, mass):
        '''信息写入文件'''
        with open('test.csv', 'a+') as f:
            f.write(str(mass) + '\n')
            f.flush()

    def pb_main(self):
        '''普通数据插入'''
        start = time.time()
        for i in range(10000):
            self.test(i)
        end = time.time()
        print('总用时间：%s' % (end - start))

    def td_main(self):
        '''多线程'''
        start = time.time()
        threads = []
        for i in self.mass:
            t = MyThread(self.test, (i,), self.test.__name__)
            threads.append(t)
        for i in self.mass:
            threads[i].start()
        for i in self.mass:
            threads[i].join()
        end = time.time()
        print('总用时间：%s' % (end - start))


if __name__ == '__main__':
    demo = Demo()
    # demo.pb_main()
    print '----------------------'
    demo.td_main()
