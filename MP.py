# Time    : 12/27/2018 9:53 AM
# Author  : Luzaofa

import time
import types
import copy_reg
import multiprocessing as mp


def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)


copy_reg.pickle(types.MethodType, _pickle_method)


class Demo(object):

    def __init__(self):
        pass

    def test(self, mass):
        '''信息写入文件'''
        with open('test.csv', 'a+') as f:
            f.writelines(str(mass) + '\n')

    def data_mp(self, func, mass):
        '''进程池'''
        pool = mp.Pool(processes=4)
        for i in mass:
            pool.apply_async(func, args=(i,))
        pool.close()
        pool.join()

    def pb_main(self):
        '''普通数据插入'''
        start = time.time()
        for i in range(10000):
            self.test(i)
        end = time.time()
        print('总用时间：%s' % (end - start))

    def mp_main(self):
        '''进程池插入'''
        start = time.time()
        self.data_mp(self.test, [i for i in range(10000)])
        end = time.time()
        print('总用时间：%s' % (end - start))


if __name__ == '__main__':
    demo = Demo()
    demo.pb_main()
    print '-----------------'
    demo.mp_main()
