#Environment Diagrams with Lambda
# 定义全局变量 a，赋值为 1
a = 1
def f(g):
    a = 2## 在 f 的局部作用域内定义局部变量 a，赋值为 2
    return lambda y: a * g(y)# 返回一个 lambda 函数：
    # 该 lambda 函数接受一个参数 y
    # 在 lambda 内部，a 取自 f 作用域（即 a = 2）
    # g(y) 调用传入的函数 g，并传入 y
   
    # 调用 f 并传入一个 lambda 函数 lambda y: a + y
# 这里的 a 是 **全局变量**，即 1
result=f(lambda y: a + y)(a)
#这里 y = 1（因为 result（a）～(1) 传入了 1）

# 打印结果
print(result)  # 输出 4


#Return Statements返回语句：

def end(n, d):
    """Print the final digits of N in reverse order until D is found."""

    while n > 0:
        last, n = n % 10, n // 10  # 获取 n 的最后一位数字，并更新 n
        print(last)  # 输出最后一位数字
        if d == last:  # 如果找到了目标数字 d
            return None  # 立即返回，终止函数执行
     #这个函数 end(n, d) 反向打印 n 的每一位数字，直到遇到 d 时停止。
	 #“反向” 是因为 n % 10 先取出最后一位，n // 10 让 n 去掉最后一位。


def search(f):#功能：接受另一个函数f，并且从0开始尝试所有整数，一直往上找，直到找到一个使得f(x)为真的值
    x = 0
    while True:
        if f(x):
            return x
        x += 1
def is_three(x):
    return x == 3

print(is_three(3))
print(search(is_three))#brute force search 蛮力搜索

def square(x):
    return x * x
def positive(x):
    return max(0, square(x) - 100)
        
print(positive(3))
print(positive(10))
print(positive(11))