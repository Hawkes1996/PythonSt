#_*_ coding: UTF-8 _*_

#题二十一：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

#分析：逆向思维

x = 1
for i in range(0,9):
    x = (x+1)*2
print x


#题二十二：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

# for a in ['x','y','z']:
#     for b in ['x','y','z']:
#         for c in ['x','y','z']:
#             if (a!=b)and(b!=c)and(a!=c)and(a!='x')and(c!='x')and(c!='z'):
#                 print'a和%s比，b和%s比，c和%s比' % (a,b,c)


#题二十三:打印出如下图案（菱形）:

# from sys import stdout
#
# for i in range(4):
#     for j in range(2-i+1):
#         stdout.write(' ')
#     for k in range(2*i+1):
#         stdout.write('*')
#     print
# for i in range(3):
#     for j in range(i+1):
#         stdout.write(' ')
#     for k in range(4-i*2+1):
#         stdout.write('*')
#     print


#题二十四：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

# a = 2.0
# b = 1.0
# sum = 0
# for n in range(0,20):
#     sum += a/b
#     temp = a
#     a= a + b
#     b = temp
#
# print  sum

# #方法二：
# a = 2.0
# b = 1.0
# l = []
# for n in range(0,20):
#     b,a = a,a + b
#     l.append(a / b)
# print reduce(lambda x,y: x + y,l)


#题二十五：求1+2!+3!+...+20!的和。

# sum = 0
# t = 1
# for n in range(1,21):
#     t *= n
#     sum += t
# print "总和为:",sum


#题二十六:利用递归方法求5!。

#分析：递归公式：fn=fn_1*4!

# def fact(j):
#     sum = 0
#     if j == 0:
#         sum = 1
#     else:
#         sum = j*fact(j-1)
#     return sum
#
# for i in range(6):
#     print '%d! = %d ' % (i,fact(i))


#题二十七：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# def output(s,n):
#     if n == 0:
#         return
#     else:
#         print(s[n-1]),
#         output(s,n-1)
#
# s = raw_input("请输入5个字符:")
# n = len(s)
# output(s,n)

# #方法二:
# def output1(s):
#     if(len(s)>0):
#         print(s[-1]),
#         output1(s[0:-1])
#
# s = raw_input("请输入5个字符:")
# output1(s)



#题二十八:有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

#分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，
# 需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。

# def age(n):
#     if n ==1 : c = 10
#     else: c = age(n-1) + 2
#     return c
#
# print age(5)


#题二十九：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

#分析：分解各个位

# x = int(raw_input("输入一个不多于5位的正整数:"))
#
# a = x / 10000
# b = x % 10000 / 1000
# c = x % 1000 / 100
# d = x % 100 / 10
# e = x % 10
#
# if a!=0:
#     print "五位数",e,d,c,b,a
# elif b!=0:
#     print "四位数",e,d,c,b
# elif c!=0:
#     print "三位数",e,d,c
# elif d!=0:
#     print "二位数",e,d
# else:
#     print "一位数",e

#方法二：
# print( '请输入大于10的数字:' )
# n=input()
# x=[]
# i=0;
#
# while(n!=0):
#     x.append(n%10)
#     i+=1
#     n/=10
#
# print( '该数有 %d 位\n' %i )
# print( '逆序为：\n')
# print( x[::] )


#题三十：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

x = int(raw_input("输入一个五位数:"))
y = str(x)
flag = True

for i in range(len(y)/2):
    if y[i] != y[-i-1]:
        flag = False
        break

if flag == True:
    print "这是一个回文数"
else:
    print "这不是一个回文数"

