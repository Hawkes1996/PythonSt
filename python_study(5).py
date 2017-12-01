# _*_ coding: UTF-8 _*_


#题四十一：模仿静态变量的用法。
#
# def varfunc():
#     var = 0
#     print 'var = %d' % var
#     var += 1
# if __name__ == '__main__':
#     for i in range(3):
#         varfunc()
#
# # 类的属性
# # 作为类的一个属性吧
# class Static:
#     StaticVar = 5
#     def varfunc(self):
#         self.StaticVar += 1
#         print self.StaticVar
#
# print Static.StaticVar
# a = Static()
# for i in range(3):
#     a.varfunc()


#题四十二：学习使用auto定义变量的用法。

#分析：没有auto关键字，使用变量作用域来举例吧。

# num = 2
# def autofunc():
#     num = 1             #局部变量
#     print '函数体num = %d' % num
#     num += 1
#
# for i in range(3):
#     print '全局变量num = %d' % num
#     num += 1
#     autofunc()


#题四十三：模仿静态变量(static)另一案例。

#分析：一个python作用域使用方法

# class Num:
#     nNum = 1
#     def inc(self):
#         self.nNum += 1
#         print '类里num = %d' % self.nNum
#
# if __name__ == '__main__':
#     nNum = 2
#     inst = Num()
#     for i in range(3):
#         nNum += 1
#         print '全局变量num = %d' % nNum
#         inst.inc()


#题四十四：两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

#分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。

# X = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# Y = [[5, 8, 1],
#      [6, 7, 3],
#      [4, 5, 9]]
#
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
#
# # 迭代输出行
# for i in range(len(X)):
#     # 迭代输出列
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#     print(r)


#题四十五：统计 1 到 100 之和。

# number = 0
# for i in range(1,101):
#     number += i
# print number
#
# print sum(range(1,101))


#题四十六：求输入数字的平方，如果平方运算后小于 50 则退出。

# def C(x):
#     return x*x
# print '如果输入的数字小于 50，程序将停止运行'

# again = True
# while again:
#     num = int(raw_input('请输入一个数字:'))
#     print '运算结果为 %d' % (C(num))
#     if C(num)>50:
#         again = True
#     else :
#         again = False


#题四十七：两个变量值互换

# def exchange(x,y):
#     x,y = y,x
#     return (x,y)
#
# if __name__ == '__main__':
#     a = 10
#     b = 20
#     print '原来的值(a=%d,b=%d)' % (a,b)
#     a,b=exchange(a,b)
#     print '交换后的值(a=%d,b=%d)' % (a,b)


#题四十八：数字比较。

# if __name__ == '__main__':
#     x = int(raw_input("请输入第一个数字:"))
#     y = int(raw_input("请输入第二个数字:"))
#     if x>y:
#         print '%d > %d' % (x,y)
#     elif x == y:
#         print '%d == %d' % (x,y)
#     elif x<y:
#         print '%d < %d' % (x,y)
#     else:
#         print '两个数无法比较!'


#题四十九：使用lambda来创建匿名函数。

# Max = lambda x,y: (x > y) * x + (x < y) * y
# Min = lambda x,y: (x > y) * y + (x < y) * x
#
# if __name__ == '__main__':
#     a = 10
#     b = 20
#     print '最大的数为 %d' % Max(a,b)
#     print '最小的数为 %d' % Min(a,b)


#题五十：输出一个随机数。

#分析：使用random模块

import random

# print random.random()               #用于生成一个0到1的随机符点数: 0 <= n < 1.0
# print random.uniform(10,20)         #用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限
# print random.randint(10,20)         #用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限
# print random.randrange(10,100,2)    #从指定范围内，按指定基数递增的集合中 获取一个随机数
# print random.choice(["JGood", "is", "a", "handsome", "boy"])    #从序列中获取一个随机元素  (列表，元组)

# p = ["Python", "is", "powerful", "simple", "and so on..."]
# random.shuffle(p)
# print p                     #random.shuffle(x[, random])，用于将一个列表中的元素打乱

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回
print slice
print list #原有序列并没有改变。              #random.sample(sequence, k)，从指定序列中随机获取指定长度的片断
