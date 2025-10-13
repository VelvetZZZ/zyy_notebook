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