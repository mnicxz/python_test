from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end-start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
        '''
        apply方法是阻塞的，当前子进程执行完后才会执行下一个进程
        apply_async方法异步非阻塞的，不用等待当前进程结束，而是随时根据系统调度来进行系统切换
        '''
    print('Waiting for all subprocesses done...')
    '''close必须在join前'''
    p.close()
    p.join()
    print('All subprocesses done.')
