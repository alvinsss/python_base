# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 19:50
# @Author  : alvin
# @File    : genvet.py
# @Software: PyCharm

import gevent
from gevent.event import Event
evt = Event()
def setter():
    '''After 3 seconds, wake all threads waiting on the value of evt'''
    print('厨师开始做菜')
    gevent.sleep(3)
    print("菜做好了")
    evt.set()  # 设置event的flag为True，所有wait的greenlet解除阻塞

def waiter(name):
    '''After 3 seconds the get call will unblock'''
    print("{} 服务员等菜".format(name))
    evt.wait()  # 阻塞，跳转到下一个greenlet
    print("菜好了, {} 送餐".format(name))

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter, "服务员 A"),
        gevent.spawn(waiter, "服务员 B"),
    ])
if __name__ == '__main__':
    main()