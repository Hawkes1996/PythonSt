#_*_ coding:utf-8 _*_

#题九十一：时间函数举例1

# if __name__ == '__main__':
#     import time
#     print time.ctime(time.time())
#     print time.asctime(time.localtime(time.time()))
#     print time.asctime(time.gmtime(time.time()))


#题九十二：时间函数举例2

# if __name__ == '__main__':
#     import time
#     start = time.time()
#
#     for i in range(3000):
#         print i
#
#     end = time.time()
#
#     print end - start


#题九十三：时间函数举例3

# if __name__ == '__main__':
#     import time
#     start = time.clock()
#     for i in range(10000):
#         print i
#     end = time.clock()
#     print 'different is %6.3f' % (end - start)


#题九十四：时间函数举例4,一个猜数游戏，判断一个人反应快慢

# if __name__ == '__main__':
#     import time
#     import random
#
#     play_it = raw_input('do you want to play it.(\'y\' or \'n\')')
#     while play_it == 'y':
#         c = raw_input('input a character:\n')
#         i = random.randint(0, 2 ** 32) % 100
#         print 'please input number you guess:\n'
#         start = time.clock()
#         a = time.time()
#         guess = int(raw_input('input your guess:\n'))
#         while guess != i:
#             if guess > i:
#                 print 'please input a little smaller'
#                 guess = int(raw_input('input your guess:\n'))
#             else:
#                 print 'please input a little bigger'
#                 guess = int(raw_input('input your guess:\n'))
#         end = time.clock()
#         b = time.time()
#         var = (end - start) / 18.2
#         print var
#         # print 'It took you %6.3 seconds' % time.difftime(b,a))
#         if var < 15:
#             print 'you are very clever!'
#         elif var < 25:
#             print 'you are normal!'
#         else:
#             print 'you are stupid!'
#         print 'Congradulations'
#         print 'The number you guess is %d' % i
#         play_it = raw_input('do you want to play it.')


#题九十五：字符串日期转换为易读的日期格式

# from dateutil import parser                       #需要安装（pip install Python-dateutil）
# dt = parser.parse("Aug 28 2015 12:00AM")
# print dt

#dateutil    第三库
#其中parser是根据字符串解析成datetime，而rrule是则是根据定义的规则来生成datetime


#题九十六：计算字符串中子串出现的次数

# if __name__ == "__main__":
#     str1 = raw_input("请输入一个字符串:")
#     str2 = raw_input("请输入其中一个子串:")
#     number = str1.count(str2)
#
#     print "子串出现的次数:",number


#题九十七：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止

# if __name__ == "__main__":
#     from sys import stdout
#     filename = raw_input("请输入文件名:\n")
#     fp = open(filename,"w")
#     str = raw_input("请输入字符串:\n")
#     while str!="#":
#         fp.write(str)
#         stdout.write(str)
#         str = raw_input('')
#     fp.close()


#题九十八：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存

# if __name__ == "__main__":
#     fp = open("test.txt","w")
#     string = raw_input("请输入一个字符串:")
#     string = string.upper()
#     fp.write(string)
#
#     fp = open("test.txt","r")
#     print fp.read()
#
#     fp.close()


#题九十九:有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
#
if __name__ == "__main__":
    import string

    fp = open('test1.txt.txt')
    x = fp.read()
    fp.close()

    fp = open('test2.txt.txt')
    y = fp.read()
    fp.close()

    fp = open("test3.txt","w")
    l = list(x+y)
    l.sort()
    s = ''
    s= s.join(l)
    fp.write(s)
    fp.close()


#题一百：列表转换为字典

# list1 = ['a','b']
# list2 = [1,2]
# print dict([list1,list2])


# i = ['a','b','c']
# l = [1,2,3]
# b = dict(zip(i,l))
# print(b)