#Rational Number Arithmetic Implementation
# 定义 rational 类型的构造器和选择器

# 构造一个有理数（用一个元组表示）
def rational(n, d):
    """构造一个有理数，n 是分子，d 是分母"""
    return (n, d)

# 获取有理数的分子
def numer(x):
    """返回有理数 x 的分子"""
    return x[0]

# 获取有理数的分母
def denom(x):
    """返回有理数 x 的分母"""
    return x[1]

# 有理数相乘
def mul_rational(x, y):
    """返回 x 与 y 的乘积"""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

# 有理数相加
def add_rational(x, y):
    """返回 x 与 y 的和"""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

# 判断两个有理数是否相等
def equal_rational(x, y):
    """判断 x 和 y 是否表示相同的有理数"""
    return numer(x) * denom(y) == numer(y) * denom(x)

# 测试
if __name__ == "__main__":
    a = rational(1, 2)
    b = rational(2, 4)
    c = add_rational(a, b)
    d = mul_rational(a, b)

    print("a =", a)
    print("b =", b)
    print("a + b =", c)
    print("a * b =", d)
    print("a == b ?", equal_rational(a, b))


    #Abstraction Barriers 抽象屏障
    #Violating Abstraction Barriers 违反抽象屏障
    add_rational([1, 2],[1, 4])#does not use constructors twice
    def divide_rational(x, y):
        return [x[0] * y[1], x[1] * y[0]]#No selectors!  20:59
    

    # 有理数运算相关函数定义

def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))

# 有理数的构造函数和选择器
def rational(n, d):
    """Construct a rational number x that represents n/d."""
    return [n, d]

def numer(x):
    """Return the numerator of rational number x."""
    return x[0]

def denom(x):
    """Return the denominator of rational number x."""
    return x[1]

# 使用示例（修正后的代码）
x, y = rational(1, 2), rational(3, 8)  
print_rational(mul_rational(x, y))

#***changed***

# 有理数运算相关函数定义

def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))

# 有理数的构造函数和选择器
def rational(n, d):
    """Construct a rational number x that represents n/d."""
    def select(name):
        if name == 'n':
            return n
        elif name =='d':
            return d
    return select

def numer(x):
    """Return the numerator of rational number x."""
    return x('n')

def denom(x):
    """Return the denominator of rational number x."""
    return x('d')

# 使用示例（修正后的代码）
x, y = rational(1, 2), rational(3, 8)  
print_rational(mul_rational(x, y))
print(x)


#Pair
pair = [1, 2]#list literal列表字面值
x, y= pair
print(x)
print(y)
#Unpacking a list 解包列表
print(pair[1])
print(pair[0])

from operator import getitem#元素选择操纵符
print(getitem(pair, 0))
print(getitem(pair, 1))



from math import gcd  # 从 fractions 模块中导入 gcd 函数（注意：Python 3.5+ 已改为 math.gcd）

def rational(n, d):
    """构造一个有理数，自动约分为最简形式"""
    g = gcd(n, d)          # 计算 n 和 d 的最大公约数
    return [n // g, d // g]  # 用整除运算约分分子分母，返回有理数（列表形式）



from math import gcd

# 构造 Rational，有理数 [numerator, denominator]，并自动约分
def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def equal_rational(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

# 示例
if __name__ == "__main__":
    a = rational(2, 4)
    b = rational(1, 2)
    print("a =", a)
    print("b =", b)
    print("a == b ?", equal_rational(a, b))




    
