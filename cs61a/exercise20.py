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

#F-stings
#String Interpolation in Python
#传统（未简化）的形式
from math import pi
'pi starts with' + str(pi) + '...'

print('pi starts with' + str(pi) + '...')

#Using string interpolation(字符串插值)
f'pi starts with {pi}...'
print(f'pi starts with {pi}...')


print(f'2 + 2 = 2 + 2')
print(f'2 + 2 = {2 + 2}')
print('2 + 2 = {2 + 2}')

f'2 + 2 = abs{2 + 2}'
print(abs)
abs = float
print(f'2 + 2 = {abs(2 + 2)}')
print(f'2 + 2 = {(lambda x: x + x)(2)}')

#在 f-string 中，每个花括号 {} 中的表达式会被单独求值，并且可能会产生副作用（side effect），从而影响后续的表达式。
s = [9, 8, 7]
print(f'because{s.pop() } {s.pop()} {str}.')

#Polymorphic Functions 多态函数
str(obj)  # obj.__str__()
repr(obj) # obj.__repr__()

"""
>>> from fractions import Fraction
>>> half = Fraction(1, 2)

>>> repr(half)
'Fraction(1, 2)'     # 这是 __repr__ 的结果

>>> str(half)
'1/2'                # 这是 __str__ 的结果

>>> half.__repr__()
'Fraction(1, 2)'

>>> half.__str__()
'1/2'
"""