def apply_twice(f, x):
    return f(f(x))


def square(x):
    return x * x


result = apply_twice(square, 2)
print(result)


def make_adder(n):#创建一个新函数并返回它   /第一个帧 
    def adder(k):
        return k + n

    return adder#将信息从本地帧带回到首次调用该函数的当前帧


add_three = make_adder(3)
print(add_three(4))#新框架：k绑定到4
print(add_three(5))
#nested framework(def statement):把函数的父级设置为该函数创建时的当前帧
#每个用户定义函数都有一个父框架 框架的父级是调用该函数的父级

"""
def f(x,y):
    return g(x)
def g(a):
    return a + y   
print(f(1,2))
"""

#Function Composition函数组合
def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f , g):
    def h(x):
        return f(g(x))
    return h
print(square(5))
print(triple(5))

squiple=compose1(square,triple)
print(squiple(5))

tripare=compose1(triple,square)
tripare(5)

squadder = compose1(square,make_adder(2))
print(squadder(3))
print(compose1(square,make_adder(2))(3))



#Lambda Expression————创建简单的函数，只评估单个表达式
x = 10
square = x * x
print(x)
print(square)

square = lambda x: x * x#将其视为一个带有形式参数x的函数，返回x*x的值
print(square(4))#只能将一个表达式作为创建lambda函数的主体
#***想在函数体内使用while语句就不能使用lambda，必须使用def*** 



#curry柯里化--将多参数函数转换为一个单参数高阶函数的行为
def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

from operator import add
print(add(2,3))

m = curry2(add)
add_three = m(3)
print(add_three(2))

curry2 = lambda f: lambda x: lambda y: f(x,y)
m = curry2(add)
print(m(2)(3))