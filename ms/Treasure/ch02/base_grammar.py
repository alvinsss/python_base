# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 20:29
# @Author  : alvin
# @File    : base_grammar.py
# @Software: PyCharm


class Base_grammar_input_output(object):
    '''
     a=1,b=2,不用中间变量交换a和b的值
    :return:
    '''

    def exchange1(self):
        a = 1
        b = 2
        a = a + b
        b = a - b
        a = a - b
        print("exchange1  a-->%d,b-->%d"%(a,b))
        print(self.__class__)

    def exchange2(self):
        a = 1
        b = 2
        a = a^b
        b = b^a
        a = a^b
        print("exchange2  a-->%d,b-->%d"%(a,b))

    def exchange3(self):
        a = 1
        b = 2
        a,b = b,a
        print("exchange3  a-->%d,b-->%d"%(a,b))

    def update_type(self):
        '''
        要修改不可变数据会出现什么问题? 抛出什么异常?
         TypeError: 'tuple' object does not support item assignment

        python对象分为可变类型与不可变类型，常见的数字、字符串、元组
        是不可变数据类型，字典、列表是可变类型。
        :return:
        '''
        a = 123
        print(id(a))
        a = 321
        print(id(a))

        li = [1,2]
        print(id(li))
        li.append(5)
        print(id(li))

        # a = (1,2)
        # a[1] = 22

    def print_callfun(self):
        '''
         print调用Python中底层的什么方法?可以看到两者还是有不同的。
            sys.stdout.write()结尾没有换行，而print()是自动换行的。另外，
            write()只接收字符串格式的参数。
            print()能接收多个参数输出，write()只能接收一个参数。
        :return:
        '''
        import sys
        print( 'hello' )
        sys.stdout.write( 'hello' )
        print( 'new' )


    def intput_lijie(self):
        print("在Python3中，input()获取用户输入，不论用户输入的是什么，获"
              "取到的都是字符串类型的。在Python2中有 raw_input()和input(), "
              "raw_input()和Python3中的input()作用是一样的，input()输入的是"
              "什么数据类型的，获取到的就是什么数据类型的")

    def for_range(self):
        A0 = dict(zip( ('a','b','c'),(1,2,3) ))
        print(A0)
        A1 = range(10)
        print(A1)

    def xran_range(self):
        print(r"两者用法相同，不同的是range返回的结果是一个列表，而xrange的结果是一个生成器"
              r"前者是直接开辟一块内存空间来保存列表,后者是边循环边使用，"
              r"只有使用时才会开辟内存空间，所以当列表很长时，使用xrange性能要比range好")

    def copy_list_dict(self):
        '''
        字典是可变对象，在下方的 l.append(a)的操作中是把字典 a的引用传到列表 l 中，当后
续操作修改a[‘num’]的值的时候，l 中的值也会跟着改变，相当于浅拷贝。
        :return:
        '''
        l = []
        for i in range(10):
            l.append({'num':i})
        print(l)

        l2 = []
        a = {'num2':0}
        for i in range(10):
            a ['num2'] =i
            l2.append(a)
        print(l2)

    def range_ge(self):
        for i in range(5,0,-1):
            print(i)

    def file_action_getdata(self):
        '''
        4G内存怎么读取一个5G的数据
        :return:
        '''
        pass

    def create_1Gfile(self):
        import os.path
        import time
        while os.path.getsize('message') < 1000000000:
            f = open('message','a')
            f.write("this is a file/n")
            f.close()
            print("file is create complted!")

    def file_read1Gfile(self):
        import time
        s_time = time.time()
        f = open('message','r')
        for i in f:
            e_time = time.time()
            print(e_time - s_time)
            break
        f.close()


class Parent(object):
    '''
1 1 1 #继承自父类的类属性x，所以都一样，指向同一块内存地址。
1 2 1 #更改Child1，Child1的x指向了新的内存地址。
3 2 3 #更改Parent，Parent的x指向了新的内存地址。
    :return:
    '''
    x=1
class Child1(Parent):

    pass
class Child2(Parent):
    pass

print (Parent.x,Child1.x,Child2.x)
Child1.x =2
print(Parent.x,Child1.x,Child2.x)
Parent.x =3
print(Parent.x,Child1.x,Child2.x)

if __name__ ==  "__main__":
    base = Base_grammar_input_output()
    base.exchange1()
    base.exchange2()
    base.exchange3()
    base.update_type()
    base.print_callfun()
    base.intput_lijie()
    base.for_range()
    base.xran_range()
    base.copy_list_dict()
    base.range_ge()
    base.create_1Gfile()
    base.file_read1Gfile()
