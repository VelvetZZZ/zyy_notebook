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
print(double('hello'))
#局部 raise 语句中断函数执行，返回到调用该函数的地方
