#*****Recursion递归*****
#Returning a Function by Its Own Names
def print_all(x):
    print(x)
    return print_all
print_all(1)(3)(5)

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum
print_sums(1)(3)(5)

#Recursive Function递归函数
"""Definition:A function is called recursive if the body of that
function calls itself,either directly or indiirectly."""
"""Implication:Executing the body of a recursive function may 
require applying that function again.当你执行一个递归函数的主体时，
可能需要你再次应用同样的函数"""
#Sum Digits Without a While Statement
def split(n):
    """Split positive n into all but its last digit and its last digit."""
    return n // 10,n % 10
all_but_last, last = split(2013)
print(all_but_last) 
print(last)

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
print (sum_digits(2013))
print (sum_digits(123456789))

def fact(n):
    if n == 0:
        return 1#0的阶乘是1
    else:
        return n * fact(n-1)
print(fact(3))#输出3*2*1

"""1.the same function fact is called multiple times.
2.Different frames keep track of the different arguments in each call.
3.What n evaluates to dapends upon which is the current environment.
4.Each call to fact solves a aimpler problem than the last:smaller n.
"""
#Iteration（while） vs Recursion  迭代vs递归


def fact_iter(n):
    total, k = 1, 1
    while k<= n:
        total, k = total*k, k+1
    return total
#Re
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


#Verifying Recursive Functions 验证递归函数的正确性

#Mutual Recursion相互递归：两个不同的函数互相调用
#luhn算法（用于计算信用卡号的校验）
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n 
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last)+ last
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last,last = split(n)
        return luhn_sum_double(all_but_last) + last
        
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last)+luhn_digit

print(luhn_sum(2))
print(luhn_sum(32))
print(luhn_sum(5105105105105100))


def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    doubled = 2 * last
    if doubled > 9:
        return sum_digits(doubled) + luhn_sum(all_but_last)  # 处理两位数的和
    else:
        return doubled + luhn_sum(all_but_last)

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

# 测试
print(luhn_sum(5105105105105100))  # 通过Luhn算法验证

#Converting Recursion to Lteration

def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum
print(sum_digits_iter(2013))





#*******迭代版
def sum_digits_iterative(n):
    total = 0           # 初始化累加器
    while n >= 10:      # 只要不是个位数就继续循环
        last = n % 10   # 取最后一位数字（即 n 的个位数）
        total += last   # 把这个个位数累加到 total 中
        n = n // 10     # 去掉 n 的最后一位，使 n 变成它的前几位
    return total + n    # 最后加上 n（当 n<10 时，它本身就是最后一位）

#递归版
def sum_digits(n):
    if n < 10:       # 如果是个位数（比如3），直接返回
        return n
    else:
        all_but_last = n // 10   # 去掉最后一位（123 → 12）
        last = n % 10            # 取最后一位（123 → 3）
        return sum_digits(all_but_last) + last  # 继续处理剩下的数字，并累加最后一位
    

# write a function that returns the factorial of n
def factorial(n):
    if n == 0:          # 0 的阶乘是 1
        return 1
    else:
        return n * factorial(n - 1)  # n 的阶乘是 n * (n-1) 的阶乘



