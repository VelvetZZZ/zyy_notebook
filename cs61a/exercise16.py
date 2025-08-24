#Generetors and Generator Functions
def plus_minus(x):
    yield x
    yield -x
t = plus_minus(3)
print(next(t))
print(next(t))

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2
t = evens(2, 10)
print(next(t))
print(next(t))
print(next(t))
print(next(t))

print(list(evens(1, 10)))

#Generators can Yield from lterators

def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x
print(list(a_then_b([3, 4],[5, 6])))

def a_then_b(a, b):
    yield from a
    yield from b
print(list(a_then_b([3, 4],[5, 6])))
#两者效果相同，后者更为简洁

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
print(list(countdown(5)))
#倒数——————
def countdown(k):
    if k > 0:
        yield k
        for x in countdown(k-1):
            yield x
t = countdown(3)
print(next(t))
print(next(t))
print(next(t))

#同理
def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'Blased off'
for k in countdown(3):
    print(k)

#生成前缀
def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
print(prefixes('both'))
print(list(prefixes('both')))

#生成子字符串
def substrings(s):
    if s:
       yield from prefixes(s) 
       yield from substrings(s[1:])
print(list(substrings('tops')))



#Yielding Partitions
#计算有多少种方法把整数 n 拆分成若干个不大于 m 的正整数的和
def count_partitions(n,m):
    """Count partitions.
    >>>count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        """基例（无效/终止条件）：如果还需分的数变成负数（说明之前选择过度），
        或者最大可用部件变为 0(不能再选任何正整数),则不可能有方案。"""
        return 0
    else:
        exact_match = 0#预置“恰好用一个 m 的那一种”的计数。此变量只在 n == m 时变成 1
        if n == m:#如果目标和 n 正好等于最大部件 m……
            exact_match = 1#……那 [m] 就是唯一且独立的一种方案，计数加 1。
        with_m = count_partitions(n-m, m)#先取出一个 m，剩下要分的是 n-m，最大部件仍是 m。递归返回“剩下部分”的方案数。
        without_m = count_partitions(n, m-1)#**完全不使用 m** 的分支：目标和仍是n，但最大部件降为 m-1。递归返回不含 m` 的方案数。
        return exact_match + with_m + without_m# 总方案数 = “恰好一个 m 的那一种” + “至少一个 m 的那些” + “完全不用 m 的那些”。
print(count_partitions(6, 4))


#输出为整数列表
def list_partitions(n, m):
    """List partitions.
    >>> for p in list_partitions(6, 4): print(p)
    [2, 4]
    定义一个函数，列出把 n 拆成若干个不超过 m 的正整数之和的所有具体方案；
    返回值是“列表的列表”。遍历并打印每一种方案。"""
    if n < 0 or m == 0:
        return []#返回空列表表示“没有方案”。
    else:#进入一般情形。
        exact_match = []#预置“恰好用一个 m 的那一种”的方案列表（可能为空）。
        if n == m:#如果 n 恰好等于 m……
            exact_match = [[m]]# ……则把唯一方案 [[m]] 放进列表里（注意两层方括号：外层是“所有方案”的列表，内层是“某个方案”的部件列表）。
        with_m = [p + [m] for p in list_partitions(n-m, m)]#把 n - m 的所有分拆方案都找出来，然后在每个方案的末尾加上一个 m，表示“我用了一个 m”。
        without_m = list_partitions(n, m-1)#生成所有“不使用 m 的分拆方案”。
        return exact_match + with_m + without_m#把所有“正好一个 m”，“用了至少一个 m”，“完全没用 m”的方案加在一起，组成最终的答案。
for p in list_partitions(6, 4):
    print(p)

#输出为字符串列表（2+4）
def partitions(n, m):
    """List partitions.
    >>>for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partitions(n-m, m)]
        without_m = partitions(n, m-1)
        return exact_match + with_m + without_m
for p in partitions(6, 4):
    print(p)

#Using yield
def partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + ' + ' + str(m)
        yield from partitions(n, m - 1)
g = partitions(60, 50)
print(next(g))   # 输出第一个结果
print(next(g))   # 输出第二个结果