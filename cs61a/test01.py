#numeral数字符号 string字符串 call expression调用表达式 operand操作数 squirreled贮藏
#assignment statements赋值语句 pow(x,y)：x的y次方
print('Hello World')

from math import pi#内置函数
print(pi)

from math import sin
print(sin)
print(sin(pi / 2))

radius = 10
print(radius)
print(2 * radius)
area, circ = pi * radius * radius, 2 * pi  * radius
print(area)
print(circ)
radius=20
print(area)#赋值的工作原理（并不同步，314是绑定到面积area的值，它不记得area曾经是用radius来定义的）
#同步请用def函数 *以下有展示（第50行）*

max(1, 2, 3)
f = max
print(f)
print(f(1,2,3))

max=7
print(f(1,2,max))

max=f
print(max(1,2,3))

from operator import add,mul
print(add)
print(mul)
#绑定名字和值的一种方式是用import语句，但他们必须是内置的名字;第二种方式是使用赋值语句
#第三种方法：使用def语句（创建自己的函数）
def square(x):
    return x * x
print(square(2))
print(square(add(3,4)))

def sum_square(x,y):
    return square(x) + square(y)
print(sum_square(3,4))



def area():
    return pi*radius*radius
print(area())
radius=10
print(area())#函数function和名字name的区别：返回表达式每次调用时都会重新评估


#Question答案：3 理解： 1、5取最大值和3取最小值，再和2取最大值，最后和4取最小值是3
f=min
f=max
g,h=min,max
max=g
print(max(f(2,g(h(1,5),3)),4))

#Defining Functions
#def<name>(<formal parameters参数值名称>):   def和冒号之间被称为function signature函数签名 *排列形式参数 函数需要多少个参数 它包含构建此本地框架所需的所有信息
    #（最简单的情况下是～注意缩进）return<return expression>  缩进后的所有内容称为function body *定义了函数的功能

#Looking up names in environments
from operator import mul
def square(square):
    return square * square
print(square(-2))
#Environment diagrams环境图 一种存储器（memory），用来记录（keep track of）名称和值之间的绑定关系
#目的：可视化解释器的过程，以便理解程序是如何执行的





#None表示某个函数未返回任何内容
def does_not_square(x):
    x * x#只是计算x乘以x但不返回它～创建了一个什么都不返回的函数None，因为没有return
    print(does_not_square(x))#解释器不会将None显示为表达式的值

#print的返回值是None，print内嵌套一个函数，会调用该函数并打印函数返回值
print(None,None)
print(print(1),print(2))






