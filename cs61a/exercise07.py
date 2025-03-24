#What Would Python Print?
from operator import add,mul
def square(x):
    return mul(x,x)

def pirate(arggg):
    print('matey')  
    def plunder(arggg):
        return arggg # 这里返回传入的参数，即 identity function 的特性
    return plunder


print(add(pirate(3)(square)(4),1))#3的作用：激活pirate函数的执行流程以及确定内部函数plunder的初始环境状态
#print(pirate(pirate(pirate))(5)(7))#错误发生在 5(7)，因为 5 不是函数！


def horse(mask):
    horse = mask#mask是原先的
    def mask(horse):
        return horse
    return horse(mask)#新定义的mask
mask = lambda horse:horse(2)
print(horse(mask))#return horse(mask)==>return mask(2)


#Implementing a Function
def remove(n,digit):
    """Return all digits of non-negative N that are no 
    DIGIT,for some non-negative DIGIT less than 10"""


    kept,digits = 0, 0
    while n > 0:
        n, last = n // 10,n % 10#//-->取整   %-->取余数
        if last != digit:
            kept = kept / 10 + last
            digits = digits + 1
    return round(kept * 10 ** (digits-1))

print(remove(231,3))



def remove(n,digit):
    """Return all digits of non-negative N that are no 
    DIGIT,for some non-negative DIGIT less than 10"""


    kept,digits = 0, 0
    while n > 0:
        n, last = n // 10,n % 10#//-->取整   %-->取余数
        if last != digit:
            kept = kept + last*10**digits
            digits = digits + 1
    return kept

print(remove(243132,2))





#Decorators装饰器 >>>装饰器本质上是一个接受函数作为参数并返回一个新函数的函数

def trace1(fn):
    """Returns a version of fn that first print
    before it is called.
    fn - a function of 1 argument(一个带参数的函数)
    """
    def traced(x):
        print('Calling', fn,'on argument', x)
        return fn(x)
    return traced

@trace1    #使用装饰器->square = trace1(square)
def square(x):
    return x * x

@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k),k + 1
    return total
print(square(12))
print(sum_squares_up_to(5))
