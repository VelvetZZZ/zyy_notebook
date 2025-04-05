#Order of Recursive Calls 递归调用的顺序
#The Cascade Function：级联函数
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)#首先打印 n 
        cascade(n//10)#调用的n除以10取整数部分
        print(n)#对cascade的递归调用后再次打印n
print(cascade(5))
print(cascade(12345))

def cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

#Inverse Cascade 反向级联函数
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)
grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

#Tree Recursion

def trace(func):
    indent = 0  # 外层变量

    def wrapper(*args, **kwargs):
        nonlocal indent  # 关键声明：允许修改外层变量
        print(" " * indent + f"-> {func.__name__}({args})")
        indent += 1
        result = func(*args, **kwargs)
        indent -= 1
        print(" " * indent + f"<- {func.__name__} 返回: {result}")
        return result

    return wrapper

@trace #在fib（0）被调用时打印出信息，当它返回时显示返回信息
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))

#Counting Partitions 计算分区

def count_partitions(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m =count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m + without_m
result = count_partitions(5, 3)
print(result)

                                






