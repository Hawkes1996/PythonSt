# _*_ coding:utf-8 _*_

#题七十一：编写input()和output()函数输入，输出5个学生的数据记录

# N = 3
#stu
# num : string
# name : string
# score[4]: list
# student = []
# for i in range(5):
#     student.append(['','',[]])
#
# def input_stu(stu):
#     for i in range(N):
#         stu[i][0] = raw_input('输入学生学号:\n')
#         stu[i][1] = raw_input('输入学生姓名:\n')
#         for j in range(3):
#             stu[i][2].append(int(raw_input('成绩:\n')))
#
# def output_stu(stu):
#     for i in range(N):
#         print '%-6s%-10s' % ( stu[i][0],stu[i][1] )
#         for j in range(3):
#             print '%-8d' % stu[i][2][j]
#
# if __name__ == '__main__':
#     input_stu(student)
#     print student
#     output_stu(student)


#题七十二：创建一个链表

# if __name__ == "__main__":
#     ptr = []
#     for i in range(5):
#         num = int(raw_input("input number:\n"))
#         ptr.append(num)
#     print ptr


#题七十三：反向输出一个链表

# if __name__ == '__main__':
#     ptr = []
#     for i in range(5):
#         num = int(raw_input('input number:\n'))
#         ptr.append(num)
#     print ptr
#
#     ptr.reverse()        #会对列表的元素进行反向排序
#     print ptr


#题七十四：列表排序及连接

#分析：排序可使用 sort() 方法，    连接可以使用 + 号或 extend() 方法

# if __name__ == '__main__':
#     a = [1, 3, 2]
#     b = [3, 4, 5]
#     a.sort()  # 对列表 a 进行排序
#     print a
#
#     # 连接列表 a 与 b
#     print a + b
#
#     # 连接列表 a 与 b
#     a.extend(b)
#     print a


#题七十五：放松一下，算一道简单的题目

# if __name__ == '__main__':
#     for i in range(5):
#         n = 0
#         if i != 1: n += 1           i=2 n+1+1=2
#         if i == 3: n += 1           i=3 n+1=3
#         if i == 4: n += 1           64+3=67
#         if i != 4: n += 1
#         if n == 3: print 64 + i


#题七十六：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

# def peven(n):
#     sum = 0
#     for i in range(2,n+1,2):
#         sum += 1.0/i
#     return sum
#
# def podd(n):
#     sum = 0
#     for i in range(1,n+1,2):
#         sum += 1.0/i
#     return sum()
#
# def jisuan(type,n):       #一个函数，把调用函数名和输入的值传入
#     sum = type(n)
#     return sum
#
# if __name__ == "__main__":
#     x = int(raw_input("请输入n的值:"))
#     if x%2 == 0:
#         sum = jisuan(peven,x)
#     else:
#         sum = jisuan(podd,x)
#
#     print "调用函数后得到的值为:",sum


#题七十七：循环输出列表

# if __name__ == "__main__":
#     s = ["man", "woman", "girl", "boy", "sister"]
#     for i in range(len(s)):
#         print s[i],

#     print
#     print '/'.join(s)


#题七十八：找到年龄最大的人，并输出。请找出程序中有什么问题

# if __name__ == '__main__':
#     person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
#     m = 'li'
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key
#     print '%s,%d' % (m, person[m])


#题七十九：字符串排序

# if __name__ == '__main__':
#     str1 = raw_input('输入第一个字符串:\n')
#     str2 = raw_input('输入第二个字符串:\n')
#     str3 = raw_input('输入第三个字符串:\n')
#
#     print str1,str2,str3
#
#     if str1 > str2: str1, str2 = str2, str1
#     if str1 > str3: str1, str3 = str3, str1
#     if str2 > str3: str2, str3 = str3, str2
#
#     print "排序后的字符串结果:"
#     print str1,str2,str3


#方法二：

# if __name__=='__main__':
#     list1=[]
#     str1=raw_input('请输入第一个字符串：')
#     str2=raw_input('请输入第二个字符串：')
#     str3=raw_input('请输入第三个字符串：')
#
#     list1.extend([str1,str2,str3])      #链接一起
#     list2=sorted(list1)          #进行排序
#
#     print '排序后的字符串为：'
#     for item in list2:
#         print item


#题八十：
# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，
# 拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，
# 拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？

# if __name__ == '__main__':
#     i = 0
#     j = 1
#     x = 0
#     while (i < 5) :
#         x = 4 * j
#         for i in range(0,5) :
#             if(x%4 != 0) :
#                 break
#             else :
#                 i += 1
#             x = (x/4) * 5 +1
#         j += 1
#     print x