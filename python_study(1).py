# -*- coding: UTF-8 -*-
#题一：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i!=j) and (j!=k) and (i!=k):
#                 print i,j,k

#题二：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

#分析：把奖金定义为成长整型

# I=int(raw_input("请输入当月利润:"))
# temp=[1000000,600000,400000,200000,100000,0]
# rate=[0.01,0.015,0.03,0.05,0.075,0.1]
# rat=0  #定义一变量，先赋值
#
# for index in range(0,6):
#     if I>temp[index]:
#         rat+=(I-temp[index])*rate[index]
#         print (I-temp[index])*rate[index]
#         i=temp[index]
# print rat

#题三：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# 分析：
# 假设该数为 x。
# 1、则：x + 100 = n2, x + 100 + 168 = m2
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。

# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)


#题四：输入某年某月某日，判断这一天是这一年的第几天？

#分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：

# year=int(raw_input('年份:\n'))
# month=int(raw_input('月份:\n'))
# day=int(raw_input('日:\n'))
#
# months=(0,31,59,90,120,151,181,212,243,273,304,334)
#
# if 0<month<=12 :
#     sum = months[month-1]
# else:
#     print"输入的日期有误!"
# sum+=day
# temp=0
# if(year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
#     temp = 1
# if(temp == 1) and (month>2):
#     sum += 1
# 2
# print year,month,day,"这是第%d天" % sum


#题五：输入三个整数x,y,z，请把这三个数由小到大输出。

# temp = []
# for i in range(3):
#     x = int(raw_input("输入数字:"))
#     temp.append()
# temp.sort()               #sort 排序函数
#
# print"排序后的结果:" ,temp

# x= raw_input("int1:")
# y= raw_input("int2:")
# Max = max(x,y)           #max比较函数
# Min = min(x,y)
# z= raw_input("int3:")
# if z > Max :
#     print Min,Max,z
# elif z < Min :
#     print z,Min,Max
# else :
#     print Min,z,Max

# #冒泡排序
# temp = []
# for i in range(5):
#     x = int(raw_input("输入数字:"))
#     temp.append(x)
#
# n = len(temp)
#
# for i in range(0,n):
#     for j in range(i,n):
#         if(temp[i]>=temp[j]):
#             temps = temp[i]
#             temp[i] = temp[j]
#             temp[j] = temps
#
# print"排序结果",temp


#题六：斐波那契数列。

#分析：又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#F0 = 0     (n=0)
#F1 = 1    (n=1)
#Fn = F[n-1]+ F[n-2](n=>2)

#方法一：
# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
#
# print fib(10)

#方法二（递归）:
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# print fib(10)

#方法三
#如果你需要输出指定个数的斐波那契数列

# def fib(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     fibs = [1, 1]
#     for i in range(2, n):
#         fibs.append(fibs[-1] + fibs[-2])
#     return fibs
#
# x = int(raw_input("输入指定个数:"))
#
# print fib(x)


#题七：将一个列表的数据复制到另一个列表中

#分析：使用列表[:]。

# #import copy
#
# temp = []
# for i in range(3):
#     x=int(raw_input())
#     temp.append(x)
#
# #temps = temp[:]
# tempss = copy.copy(temp)
#
# print tempss


#题八：输出 9*9 乘法口诀表。

# for i in range(1,10):
#     print  #空行
#     for j in range(1,i+1):
#         print "%d*%d=%d" % (i,j,i*j),


#题九：暂停一秒输出。

#分析：使用 time 模块的 sleep() 函数。

# import time
#
# temp=[1,2,3,4]
# for i in range(len(temp)):
#     print temp[i]
#     time.sleep(1)


#题十：暂停一秒输出，并格式化当前时间。

import time

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 暂停一秒
time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


