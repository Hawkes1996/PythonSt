#_*_ coding:utf-8 _*_

#题八十一：809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果

# a = 809
# for i in range(10,100):
#     b = i * a + 1
#     if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
#         print b,'/',i,' = 809 * ',i,' + ', b % i


#题八十二：八进制转换为十进制

# if __name__ == '__main__':
#     n = 0
#     p = raw_input('input a octal number:\n')
#     for i in range(len(p)):
#         n = n * 8 + ord(p[i]) - ord('0')
#     print n


#题八十三：求0—7所能组成的奇数个数

# if __name__ == '__main__':
#     sum = 4
#     s = 4
#     for j in range(2,9):
#         print "%d位时的个数" % j,sum
#         if j <= 2:
#             s *= 7
#         else:
#             s *= 8
#         sum += s
#     print '总数 = %d' % sum


#题八十四：连接字符串

# delimiter = ','
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print delimiter.join(mylist)


#题八十五：输入一个正整数，然后判断最少几个 9 除于该数的结果为整数

# num = int(raw_input("输入一个正整数:"))
#
# temp = 9
# sum = 1
#
# while(1):
#     if temp%num == 0:
#         break
#     else:
#         temp = temp*10 + 9
#         sum = sum + 1
#
# print "最少%d个9除于该数的结果为整数" % sum


#题八十六：两个字符串连接程序

# if __name__ == "__main__":
#     x1 = "abc"
#     x2 = "def"
#
#     x3 = x1 + x2
#     print x3


#题八十七：回答结果（结构体变量传递）

# if __name__ == '__main__':
#
#     class student:
#         x = 0
#         c = 0
#
#     def f(stu):
#         stu.x = 20
#         stu.c = 'c'
#
#     a= student()
#     a.x = 3
#     a.c = 'a'
#     f(a)
#     print a.x,a.c


#题八十八：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的*

# if __name__ == "__main__":
#     n = 1
#     while n<=7:
#         x = int(raw_input("输入一个值:"))
#         while x<1 or x>50:
#             x = int(raw_input("输入的值有误，重新输入:"))
#         print x * '*'
#         n += 1


#题八十九：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换

# from sys import stdout
# if __name__ == "__main__":
#     x = int(raw_input("输入四位的整数:"))
#     temp = []
#     temp.append(x%10)  #个位数
#     temp.append(x%100/10)
#     temp.append(x%1000/100)
#     temp.append(x/1000)
#
#     for i in range(4):
#         temp[i] += 5
#         temp[i] %= 10
#
#     for i in range(2):
#         temp[i],temp[3-i] = temp[3-i],temp[i]
#     print "加密后的结果：",
#     for i in range(3,-1,-1):
#         stdout.write(str(temp[i]))

#题九十：列表使用实例

# list
# 新建列表
testList = [10086, '中国移动', [1, 2, 4, 5]]

# 访问列表长度
print len(testList)
# 到列表结尾
print testList[1:]
# 向列表添加元素
testList.append('i\'m new here!')

print len(testList)
print testList[-1]
# 弹出列表的最后一个元素
print testList.pop(1)
print len(testList)
print testList



# list comprehension
# 后面有介绍，暂时掠过
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print matrix
print matrix[1]
col2 = [row[1] for row in matrix]  # get a  column from a matrix
print col2
col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # filter odd item
print col2even