#CONTROL
#life cycle of a User-Defined Function
#1.def statement 2.call expression 3.calling/applying


from operator import mul
def square(x):
    return mul(x, x)


print(square(square(3)))

#multiple environments in one diagram
#the global frame-全局框架（环境中的最后一个框架）  the parent of this frame-这个框架的父级
#*names have no meaning without environments*  每个表达式都在一个环境的上下文中评估---使我们弄清名称的含义
#同名变量优先级：A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found
#名称评估为在当前环境中找到该名称的最早（中文理解应该是最后一个框架里的）框架中绑定到该名称的值
from operator import mul


def square(square):
    return mul(square, square)


print(square(4))  #没有缩进，表明它在全局框架中被评估
#参数名与函数名相同在 def square(square): 这一行，square 既是函数名，又是参数名。这样做不会直接导致语法错误，但可能会让初学者感到困惑。

#division除法
print(2013 / 10)  #true division 结果必是浮点数
print(2013 // 10)  #integer division 整数除法 取整
#对应
from operator import truediv, floordiv

print(truediv(3, 4))
print(floordiv(3, 4))
#mod运算符
print(2013 % 10)  #取余
#对应
from operator import mod

print(mod(3, 4))


def divide_exact(a, b):
    return a // b, a % b


quotient, remainder = divide_exact(3, 4)
print(quotient)
print(remainder)

from operator import floordiv, mod


def divide_exact(a, b=10):  #如果没有传入参数绑定到d，那么我将把10绑定到b
    return floordiv(a, b), mod(a, b)


q, r = divide_exact(2013, 10)
print("Quotient=", q)
print("Remainder=", r)
#在定义函数时，你可以给出所谓的默认值（default values）：一个占位符placeholder用来表示形式参数后放置的默认值
q, r = divide_exact(2013)
print("Quotient=", q)
print("Remainder=", r)


#statements语句  第一个标题确定了语句的类型
#conditional statement条件语句
def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
x=-2
print(absolute_value(x))
x=999
print(absolute_value(x))#可以有0个或多个elif子句/0个或1个else子句，*但else必须在最后*
#false values假值 in python:False,0,'',None
#true values真值 in python：anything else(true)



#lteration迭代🔁
#While statement循环语句
i,total=0,0
while i<3:
    i=i+1
    total=total+i
    print(i,total)

