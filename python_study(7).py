# _*_ coding:UTF-8 _*_

#题六十一：打印出杨辉三角形（要求打印出10行）

# if __name__ == '__main__':
#     x = []
#     for i in range(10):
#         x.append([])
#         for j in range(10):
#             x[i].append(0)          #初始化一个二维数组
#
#     for i in range(10):
#         x[i][0] = 1
#         x[i][i] = 1                 #第一个和最后一个赋值为1
#
#     for i in range(2,10):
#         for j in range(1,i):
#             x[i][j] = x[i-1][j-1] + x[i-1][j]       #第二个开始为上一行的第一个和第一个的和
#
#     from sys import stdout
#     for i in range(10):
#         for j in range(i+1):
#             stdout.write(str(x[i][j]))
#             stdout.write(' ')  #print ' ',
#         print

#方法二（递归函数）：

# n =10
# def lst(i,j):
#     if i==j or j==1:
#         return 1
#     else:
#         return lst(i-1,j-1) + lst(i-1,j)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print lst(i,j),
#     print


#题六十二：查找字符串

# temp1 = 'abcdefg'
# temp2 = 'cde'
#
# print temp1.find(temp2)


#Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
#则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
#str.find(str, beg=0, end=len(string))


#题六十三：画椭圆

#分析：使用Tkinter

# if __name__ == '__main__':
#     from Tkinter import *
#
#     x = 360
#     y = 160
#     top = y - 30
#     bottom = y - 30
#
#     canvas = Canvas(width=400, height=600, bg='white')
#     for i in range(20):
#         canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
#         top -= 5
#         bottom += 5
#     canvas.pack()
#     mainloop()


#题六十四：利用ellipse 和 rectangle 画图

# if __name__ == '__main__':
#     from Tkinter import *
#     canvas = Canvas(width = 400,height = 600,bg = 'white')
#     left = 20
#     right = 50
#     top = 50
#     num = 15
#     for i in range(num):
#         canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
#         canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
#         canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
#         right += 5
#         left += 5
#         top += 10
#
#     canvas.pack()
#     mainloop()


#题六十五：一个最优美的图案

# import math
# class PTS:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
# points = []
#
# def LineToDemo():
#     from Tkinter import *
#     screenx = 400
#     screeny = 400
#     canvas = Canvas(width = screenx,height = screeny,bg = 'white')
#
#     AspectRatio = 0.85
#     MAXPTS = 15
#     h = screeny
#     w = screenx
#     xcenter = w / 2
#     ycenter = h / 2
#     radius = (h - 30) / (AspectRatio * 2) - 20
#     step = 360 / MAXPTS
#     angle = 0.0
#     for i in range(MAXPTS):
#         rads = angle * math.pi / 180.0
#         p = PTS()
#         p.x = xcenter + int(math.cos(rads) * radius)
#         p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
#         angle += step
#         points.append(p)
#     canvas.create_oval(xcenter - radius,ycenter - radius,
#                        xcenter + radius,ycenter + radius)
#     for i in range(MAXPTS):
#         for j in range(i,MAXPTS):
#             canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)
#
#     canvas.pack()
#     mainloop()
# if __name__ == '__main__':
#     LineToDemo()


#题六十六：输入3个数a,b,c，按大小顺序输出

# a = int(raw_input("请输入a的值:"))
# b = int(raw_input("请输入b的值:"))
# c = int(raw_input("请输入c的值:"))
#
# def swap(x,y):
#     return y,x
#
# if a>b : a,b = swap(a,b)
# if a>c : a,c = swap(a,c)
# if b>c : b,c = swap(b,c)
#
# print a,b,c


# x = []
# for i in range(3):
#     n = int(raw_input("输入一个数:"))
#     x.append(n)
#
# x.sort()
# print x

#   从大到小
# if __name__=='__main__':
#     l=[]
#     for i in range(3):
#         x=raw_input('输入一个数字:')
#         l.append(x)
#     for i in range(3):
#         print(max(l)),
#         l.remove(max(l))  #利用 remove（）函数依次输出最大值


#题六十七：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组

# a=[1,2,3,7,9,8]
#
# for i in range(len(a)):
#     if a[i]==max(a):
#     	a[0],a[i]=a[i],a[0]     #最大的和第一个交换
#
# for i in range(len(a)):
#     if a[i]==min(a):
#         a[i],a[len(a)-1]=a[len(a)-1],a[i]   #最小的和最后一个交换
#
# print a


#题六十八：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

# from collections import deque
#
# m = int(raw_input("输入后移的数:"))
# x = [1,2,3,4,5,6,7]     # 7 个数
#
# temp = deque(x)
# temp.rotate(m)
#
# print list(temp)


#方法二

# x = [1,2,3,4,5,6,7]
# m = int(raw_input("输入后移的数:"))
#
# def rot(x,n):
#     l = len(x)
#     n = l-n
#
#     return x[n:l] + x[0:n]
#
# b = rot(x,m)
#
# print x
# print b
#
# print len(x)
# print x[4:6]


#题六十九：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位

# n=int(input("输入人数:"))
# List=[]
# for i in range(1,n+1):
#     List.append(i)
#
# sum=0
#
# while 1:
#     t=0;
#     for i in range(1,len(List)+1):
#         sum=sum+1
#         if (sum)%3==0:
#             List.pop(i-1-t)
#             t=t+1
#
#     if len(List)==1:
#         print("最后留下的是原来第%d号的那位" % List[0])
#         break


#题七十:写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度

# if __name__ == '__main__':
#     str = raw_input("请输入一个字符串:")
#     print "字符串的长度为",len(str)