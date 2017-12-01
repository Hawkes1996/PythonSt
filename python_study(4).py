#-*_ coding: UTF-8 _*_

#题三十一：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# letter = raw_input("输入第一字母：")
#
# if letter == 'S':
#     letter = raw_input("请输入第二字母:")
#     if letter == 'a':
#         print ('Saturday')
#     elif letter == 'u':
#         print ('Sunday')
#     else:
#         print ('输入的星期有误')
#
# elif letter == 'F':
#     print ('Friday')
#
# elif letter == 'M':
#     print ('Monday')
#
# elif letter == 'T':
#     letter = raw_input("请输入第二个字母:")
#
#     if letter == 'u':
#         print ('Tuesday')
#     elif letter == 'h':
#         print ('Thursday')
#     else:
#         print ('输入的星期有误')
#
# elif letter == 'W':
#     print ('Wednesday')
# else:
#     print ('输入的星期有误')


#题三十二：按相反的顺序输出列表的值。

# x = ['one','two','three',1,2,3]
# for i in x[::-1]:                #list[::-1] 倒序
#     print i


#题三十三：按逗号分隔列表。

# x = [1,2,3,4]
# print ','.join(str(n) for n in x)


#题三十四：练习函数调用。

# def hello_world():
#     print 'hello world'
#
# def three_hellos():
#     for i in range(3):
#         hello_world()

# if __name__ == '__main__':
#     three_hellos()


#题三十五:文本颜色设置

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print bcolors.WARNING + "警告的颜色字体?" + bcolors.HEADER + "   #粉红色"


#题三十六：求100之内的素数。

# min = int(raw_input("输入区间最小值:"))
# max = int(raw_input("输入区间最大值:"))
#
# for x in range(min,max+1):
#     if x>1 :
#         for y in range(2,x):
#             if(x % y) == 0:
#                 break
#         else:
#             print (x)


#题三十七：对10个数进行排序。
#
# print "输入十个数"
# temp = []
# for i in range(10):
#     temp.append(int(raw_input("输入数字:")))
# temp.sort()
# print temp
#
# #方法二：

# a = []
# for i in range(10):
#     a.append(input("输入数字:"))
# print a
#
# for i in range(9):
#     for j in range(i+1,10):
#         if a[i] > a[j]:
#             a[i],a[j] = a[j],a[i]
# print a


#题三十八：求一个3*3矩阵对角线元素之和。

# if __name__ == '__main__':
#     temp = []
#     sum = 0.0
#     for i in range(3):
#         temp.append([])
#         for j in range(3):
#             temp[i].append(float(raw_input()))
#     for i in range(3):
#         sum += temp[i][i]
# print sum


#题三十九：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

#分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

if __name__ == '__main__':
    # 方法一 ： 0 作为加入数字的占位符
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print '原始列表:'
    for i in range(len(a)):
        print a[i],
    number = int(raw_input("\n插入一个数字:\n"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    print '排序后列表:'
    for i in range(11):
        print a[i],


#题四十：将一个数组逆序输出。

#分析：用第一个和最后一个交换

# if __name__ == '__main__':
#     a = [9,6,5,4,1]
#     N = len(a)
#     print a
#     for i in range(len(a) / 2):
#         a[i],a[N - i - 1] = a[N - i - 1],a[i]
#     print a

# #方法二：
# if __name__ == '__main__':
# 	a = [9,6,5,4,1]
# 	print a[::-1]
#
# #方法三：
a = [9,6,5,4,1]
a.reverse()
print a