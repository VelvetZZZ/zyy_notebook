#literation：Fibonacci sequence(斐波那契数列）

def fib(n):
    """Compute the nth Fibonacci number, for N > 1."""
    pred, curr = 0, 1  # 0th & 1st Fibonacci numbers
    k = 1  # curr is the kth Fibonacci number
    while k < n:
        pred, curr = curr, pred + curr  #***注意赋值！
        k += 1  # k = k + 1
    return curr  #计算机默认数是从0开始的所以会用curr不是pred***


print(fib(3))

#Control statements控制语句：if、 while
#if_(,,,)~~~if-call statement: if调用表达式（和if语句的对比如下）
from math import sqrt#built-in square root function内置的平方根函数


def real_sqrt(x):
    """Return the real square root of x."""
    if x >= 0:
        return sqrt(x)
    else:
        return 0#负数的平方根是虚数，虚数的实部是0
print(real_sqrt(-16))#请确保 print 语句与函数定义在同一级别，而不是缩进在函数定义内部*

###if调用表达式要定义
def if_(c,t,f):
    if c:
        return t
    else:
        return f
from math import sqrt
def real_sqrt(x):
    """Return the real square root of x."""
    return if_(x >= 0, sqrt(x),0)
print(real_sqrt(16))
#会报错：print(real_sqrt(-16))#每个子表达式都评估

from math import sqrt
def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10
print(has_big_sqrt(1000))
print(has_big_sqrt(-1000))


#and,or**and左假听左，or左真听左，听左则友式不被计算
from math import sqrt
def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10#判断x的平方根是否大于10
def reasonable(n):
    return n == 0 or 1/n != 0#n等于0或者1除以n不等于0，意味着它不太大，不至于被四舍五入为0，那么n就是合理的
print(reasonable(1000))
print(reasonable(1000**10000))#short-circuiting短路行为



"""Generalization"""
from math import sqrt,pi
def area_square(r):
    return r*r
def area_circle(r):
    return r*r*pi
def area_hexagon(r):
    return r*r*3*sqrt(3)/2
print(area_hexagon(10))
print(area_hexagon(-10))#*不太对，要调整


#assert断言语句
assert 3 > 2,'Math is broken'#如果该表达式为假，那么每当用户运行程序时都会打印一个错误信息
#assert 2 > 3,'Math is false'#错误显示



#运用assert调整之后
from math import sqrt,pi

def area(r,shape_constant):
    assert r > 0, 'A length must be positive'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)
def area_circle(r):
    return area(r,pi)
def area_hexagon(r):
    return area(r, 3 * sqrt(3)/2)
print(area_hexagon(10))
#print(area_hexagon(-10))#错误显示

#Generalizing Over Computational Processes概括计算过程
def identity(k):
    return k
def cube(k):
    return pow(k,3)
def summation(n,term):
    """Sum the first N terms of a sequence. """
    total,k = 0,1
    while k <= n:
        total,k=total+term(k),k+1
    return total


def sum_naturals(n):#对自然数进行函数化 对前n个自然数求和
    """Sum the first N natural numbers.
    sum_naturals(5)
    15
    """
    return summation(n,identity)

def sum_cubes(n):#求自然数的前n个立方和
    """Sum the first N cubes of natural numbers.
    sum_cubes(5)
    225"""
    return summation(n,cube)
print(sum_naturals(5))
print(sum_cubes(5))


#定义一个返回函数的函数
def make_adder(n):
    """Return a function that takes one argument,
    K and return K+N
    >>> add_three=make_adder(3)
    >>> add_three(5)
    8
    """
    def adder(k):
        return k+n
    return adder
print(make_adder(3)(1))
#函数可作参数传递，可作返回值返回
#Higher-order function高阶函数：表达计算的一般方法/消除程序中的重复/在函数之间分离关注点





