#Exceptions
#Raise Statements
#raise TypeError('very bad idea')
#全局 raise 语句直接中断程序执行

def double(x):
    if isinstance(x, str):
        raise TypeError('double takes only numbers')
    return x * 2
print(double(3))
#print(double('hello')) # Uncomment to see the error
#局部 raise 语句中断函数执行，返回到调用该函数的地方
try:
    print(double('hello'))
except TypeError as e:
    print('caught error:', e)

print('Program continues...')
#函数内的 raise 会中断函数本身的执行；如果外层没有捕获这个异常，整个程序就会终止。

#Try Statement
#Handling Exceptions
try:
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0
print(x)


def invert(x):
    result = 1/x
    print('Never printed if x is 0')
    return result
print(invert(2))
# print(invert(0)) # Uncomment to see the error

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)
a = invert_safe(2)
print(a)
b = invert_safe(0)
print(b)

#Example：Reduce
#Reducing a Sequence to a Value
from operator import truediv, mul, add
def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
    
def reduce(f, s, initial):
    """Combine elements of s using f starting with initial.
    >>> reduce(mul,[2, 4, 8], 1)
    64
    >>>reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial#迭代实现

def reduce(f, s, initial):
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))#递归实现
    

print(divide_all(1024,[2, 4, 0, 8]))
print(divide_all(1024,[2, 4, 8]))

#Programming Languages
#Parsing 解析
#Scheme-Syntax Calculator
#Evaluation 计算
#The Eval Function
from operator import add, sub, mul, truediv
from functools import reduce

# Helper: Convert Python list to Scheme-style linked list (for demo purposes)
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __repr__(self):
        return f"Pair({self.first}, {self.rest})"

nil = None  # Scheme’s empty list representation

def as_scheme_list(*args):
    """Convert Python values to nested Pair linked list."""
    if not args:
        return nil
    first, *rest = args
    return Pair(first, as_scheme_list(*rest))

# --------------------------------------------------
# calc_apply: Apply operator to argument list
# --------------------------------------------------
def calc_apply(operator, args):
    """Apply the named operator to a list of args."""
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')

    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return -args[0]
        else:
            return reduce(sub, args[1:], args[0])
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return 1 / args[0]
        else:
            return reduce(truediv, args[1:], args[0])
    else:
        raise TypeError(operator + ' is an unknown operator')

# --------------------------------------------------
# 测试示例（对应讲师演示内容）
# --------------------------------------------------
print(calc_apply('+', [1, 2, 3]))        # 6
print(calc_apply('-', [10, 2, 3]))       # 5
print(calc_apply('*', [2, 3, 4]))        # 24
print(calc_apply('/', [100, 4]))         # 25.0
print(calc_apply('/', [1024, 2, 2, 2, 2]))  # 64.0

# 错误情况
try:
    print(calc_apply('?', [2, 3]))
except Exception as e:
    print('Error:', e)

try:
    print(calc_apply('-', []))
except Exception as e:
    print('Error:', e)




    
#Interactive Interpreters


    
