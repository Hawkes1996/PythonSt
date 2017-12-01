#_*_ coding: UTF-8  _*_

#题十一：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？

#分析：兔子的规律为数列1,1,2,3,5,8,13,21....

# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print '%12d %12ld' % (f1,f2),
#     if (i % 3) == 0:
#         print ''
#     f1 = f1 + f2
#     f2 = f1 + f2


#题十二：判断101-200之间有多少个素数，并输出所有素数。

#分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

# temp = []
# for i in range(101,200):
#     for j in range(3,i-1):
#         if i%j == 0:
#             break
#     else:
#         temp.append(i)
#
# print temp
# print "素数有%d个" % len(temp)


#题十三：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

#分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。

# for n in range(100,999):
#     a = n/100          #百分位
#     b = n/10 %10       #十分位
#     c = n%10           #个位
#     if n == a ** 3 + b**3 + c**3:
#         print n


#题十四：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

#分析：
# 1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
#(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
#(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。


# x = int(raw_input("输入要分解的正整数:"))
# x1 = x
# temp = []
# if x<=1:
#     print "输入正确的正整数"
# while x>1:
#     for i in range(2,x+1):
#         if x%i == 0:
#             x = x/i
#             temp.append(str(i))
#             break
# print '%d = ' % x1 + '*'.join(temp)    #join函数：  'sep'.join(seq)    sep：分隔符。可以为空
                                                                        #seq：要连接的元素序列、字符串、元组、字典


#题十五：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示

# score = int(raw_input("请输入成绩:"))
#
# if score>=90:
#     grade = 'A'
# elif score>=60:
#     grade = 'B'
# else:
#     grade = 'C'
#
# print "该同学成绩等级为 %s" % grade


#题十六：输出指定格式的日期。

# import datetime
#
# if __name__ == '__main__':
#     # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
#     print(datetime.date.today().strftime('%d/%m/%Y'))
#
#     # 创建日期对象
#     miyazakiBirthDate = datetime.date(1941, 1, 5)
#
#     print(miyazakiBirthDate.strftime('%d/%m/%Y'))
#
#     # 日期算术运算
#     miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
#
#     print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
#
#     # 日期替换
#     miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
#
#     print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))


#题十七：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

#分析：利用while语句,条件为输入的字符不为'\n'。

# import  string
#
# s = raw_input("请输入一行字符:")
# letters = 0
# space = 0
# number = 0
# others = 0
#
# for x in s:
#     if x.isalpha():
#         letters += 1
#     elif x.isspace():
#         space += 1
#     elif x.isalnum():
#         number += 1
#     else:
#         others += 1
#
# print "这行字符中 英文字母有%d,空格有%d,数字有%d,其他字符有%d" % (letters,space,number,others)


#题十八:求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

# sum = []
# Tn = 0
# a = int(raw_input("输入a的值:"))
# n = int(raw_input("输入个数:"))
# for count in range(n):
#     Tn = Tn + a
#     a = a * 10
#     sum.append(Tn)
#
# sum = reduce(lambda x,y:x+y,sum)  #reduce函数 ： reduce(函数,list) 函数参数必须有两个
# print "计算的总值为",sum


#题十九：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。


# for i in range(2,1001):
#     temp = []
#     sum = 0
#     for j in range(1,i):
#         if i%j == 0:
#             sum += j
#             temp.append(j)
#     if sum == i:
#         print i,temp


#题二十：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height = []         #纪录每一次的高度
tour = []           #记录总的经过的距离

start_height = 100.0 #赋值为浮点型
times = 10

for i in range(1,times+1):
    if i == 1:
        tour.append(start_height)
    else:
        tour.append(2*start_height)
    start_height /= 2
    height.append(start_height)

print '总的高度：',sum(tour)
print '第十次的高度为：',height[-1]

