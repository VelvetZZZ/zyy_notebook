#String Representations 字符串表示
#The repr String for an Object
print(12e12)
#The str String for an Object
from fractions import Fraction
half = Fraction(1, 2)
print(repr(half))
print(str(half))
print(half)
print(type(str(half)))  # 输出：<class 'str'>
print(eval(repr(half)))
print(eval(str(half)))# 输出：浮点数 0.5


s = "Hello World"
print(s)
print(str(s))
print(repr(s))
repr(s)#"'Hello, World'"
