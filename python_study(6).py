#_*_ coding: UTF－8 _*_

#题五十一：学习使用按位与 &

#分析：0&0=0;  0&1=0;  1&0=0;  1&1=1

# if __name__ == '__main__':
#     a = 077
#     b = a & 3
#     print 'a & b = %d' % b
#     b &= 7
#     print 'a & b = %d' % b


#题五十二：学习使用按位或 |

#分析：0|0=0;  0|1=1;  1|0=1;  1|1=1

# if __name__ == '__main__':
#     a = 077
#     b = a | 3
#     print 'a | b is %d' % b
#     b |= 7
#     print 'a | b is %d' % b

#题五十三：学习使用按位异或 ^

#分析：0^0=0;  0^1=1;  1^0=1;  1^1=0

# if __name__ == '__main__':
#     a = 077
#     b = a ^ 3
#     print 'The a ^ 3 = %d' % b
#     b ^= 7
#     print 'The a ^ b = %d' % b


#题五十四：取一个整数a从右端开始的4〜7位

#分析：
# 1)先使a右移4位。
# 2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
# 3)将上面二者进行&运算。

# if __name__=='__main__':
#     a = int(raw_input("请输入整数a的值:"))
#     b = a >> 4
#     c = ~(~0 << 4)
#     d = b & c
#     print '%o\t%o' % (a, d)


#题五十五：学习使用按位取反~。

#分析：~0=1; ~1=0;
# (1)先使a右移4位。
# (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
# (3)将上面二者进行&运算

# if __name__ == '__main__':
#     a = 234
#     b = ~a
#     print 'The a\'s 1 complement is %d' % b
#     a = ~a
#     print 'The a\'s 2 complement is %d' % a


#题五十六：画图，学用circle画圆形

# if __name__ == '__main__':
#     from Tkinter import *
#
#     canvas = Canvas(width=400, height=400, bg='yellow')
#     canvas.pack(expand=YES, fill=BOTH)
#     k = 1
#     j = 1
#     for i in range(0, 26):
#         canvas.create_oval(210 - k, 190 - k, 210 + k, 190 + k, width=1)
#         k += j
#         j += 0.3
#
#     mainloop()


#使用turtle模块：
# if __name__ == '__main__':
#     import turtle
#     turtle.title("画圆")
#     turtle.setup(800,600,0,0)
#     pen=turtle.Turtle()
#     pen.color("yellow")
#     pen.width(5)
#     pen.shape("turtle")
#     pen.speed(1)
#     pen.circle(100)


#题五十七：画图，学用line画直线

# if __name__ == '__main__':
#     from Tkinter import *
#
#     canvas = Canvas(width=300, height=300, bg='green')
#     canvas.pack(expand=YES, fill=BOTH)
#     x0 = 263
#     y0 = 263
#     y1 = 275
#     x1 = 275
#     for i in range(19):
#         canvas.create_line(x0,y0,x0,y1, width=1, fill='red')
#         x0 = x0 - 5
#         y0 = y0 - 5
#         x1 = x1 + 5
#         y1 = y1 + 5
#
#     x0 = 263
#     y1 = 275
#     y0 = 263
#     for i in range(21):
#         canvas.create_line(x0,y0,x0,y1,fill = 'red')
#         x0 += 5
#         y0 += 5
#         y1 += 5
#
#     mainloop()


#题五十八：画图，学用rectangle画方形

#分析：rectangle(int left, int top, int right, int bottom)
#参数说明：(left ，top )为矩形的左上坐标，(right,bottom)为矩形的右下坐标，两者可确定一个矩形的大小

# if __name__ == '__main__':
#     from Tkinter import *
#
#     root = Tk()
#     root.title('Canvas')
#     canvas = Canvas(root, width=400, height=400, bg='yellow')
#     x0 = 263
#     y0 = 263
#     y1 = 275
#     x1 = 275
#     for i in range(19):
#         canvas.create_rectangle(x0, y0, x1, y1)
#         x0 -= 5
#         y0 -= 5
#         x1 += 5
#         y1 += 5
#
#     canvas.pack()
#     root.mainloop()


#题五十九：画图

#分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位

# if __name__ == '__main__':
#     from Tkinter import *
#
#     canvas = Canvas(width=300, height=300, bg='green')
#     canvas.pack(expand=YES, fill=BOTH)
#     x0 = 150
#     y0 = 100
#     canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
#     canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
#     canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
#     import math
#
#     B = 0.809
#     for i in range(16):
#         a = 2 * math.pi / 16 * i
#         x = math.ceil(x0 + 48 * math.cos(a))
#         y = math.ceil(y0 + 48 * math.sin(a) * B)
#         canvas.create_line(x0, y0, x, y, fill='red')
#     canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)
#
#     for k in range(501):
#         for i in range(17):
#             a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
#             x = math.ceil(x0 + 48 * math.cos(a))
#             y = math.ceil(y0 + 48 + math.sin(a) * B)
#             canvas.create_line(x0, y0, x, y, fill='red')
#         for j in range(51):
#             a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
#             x = math.ceil(x0 + 48 * math.cos(a))
#             y = math.ceil(y0 + 48 * math.sin(a) * B)
#             canvas.create_line(x0, y0, x, y, fill='red')
#     mainloop()


#题六十：计算字符串长度

ptr = 'strlen'
print '字符串长度:',len(ptr)