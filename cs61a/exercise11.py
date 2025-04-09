#Box-and-Pointer Notation 方框和指针表示法
"""在环境图中表示列表的一种方式"""

#Slicing 切片-> 可以对列表和范围等序列执行的操作
odds = [3, 5, 7, 9, 11]
sth=list(range(1, 3))
print(sth)

sth=[odds[i] for i in range (1, 3)]
print(sth)

#slicing
print(odds[1:3])
print(odds[:3])
print(odds[1:])
print(odds[:])
#Slicing Creates New Values
#Processing Container Values 处理容器值
#Sequence Aggregation*序列聚合

#sum(iterable[, start]) -> value
print(sum([2, 3, 4]))#对字符串不起作用

print([2, 3] + [4])
print(sum([[2, 3] + [4]],[]))#提供起始值进行求和
print([] + [2, 3] + [4])

#max(iterable[, key=func])-> value
#max(a, b, c, ...[, key=func])-> value
print(max(range(5)))
print(max(0, 1, 2, 3, 4))
print(max(range(10), key=lambda x: 7-(x-4)*(x-2)))#在这个范围内key function输出的最大值为3

#all-> bool(判断真假值)
print(all([x < 5 for x in range(5)]))
print(all(range(5)))#0 is false

#Strings 字符串
#Strings are an Abstraction 是文本数据的表示
print('curry = lambda f: lambda x: lambda y: f(x, y)')
print(exec('curry = lambda f: lambda x: lambda y: f(x, y)'))

from operator import add
print(curry(add)(3)(4))

city = 'Berkeley'
print(len(city))
print(city[3])

print('here'in "where's Waldo?")
print(234 in [1, 2, 3, 4, 5])
print([2, 3, 4] in [1, 2, 3, 4, 5])
#When working with strings, we usually care about whole words more than letters

#Dictionaries字典
numerals = {'I':1, 'V':5, 'X':10}#可以使用数字或字符串作为键或值
print(numerals['X'])
print(numerals['V'])
#Dictionaries go only one way
"""Dictionaries are sequences of keys"""
print(list(numerals))

print(numerals.values())
print(sum(numerals.values()))
print(list(numerals.values()))


{1: 'item'}
# 一个最基础的字典，键为整数 1，值为字符串 'item'
{1: ['first', 'second'], 3: 'third'}
# 键1对应一个列表，键3对应字符串
d = {1: ['first', 'second'], 3: 'third'}
print(d[1])   # 输出 ['first', 'second']
print(d[3])   # 输出 'third'

len(d)     # 输出 2，说明有两个键
len(d[1])  # 输出 2，键1对应的列表有两个元素
len(d[3])  # 输出 5，因为 'third' 是 5 个字符长

#Dictionary Comprehensions 字典推导式
# Python字典推导式详解

## 1. **字典推导式的基本语法**
### 核心结构
"""{ <键表达式>: <值表达式> for <变量> in <可迭代对象> if <过滤条件> }
#简单版
{ <键表达式>: <值表达式> for <变量> in <可迭代对象> }
"""
# 列表推导式
print([x**2 for x in range(5)]) #输出列表[0, 1, 4, 9, 16]

# 字典推导式
print({x: x**2 for x in range(5)}) #输出字典 {0:0, 1:1, 2:4, 3:9, 4:16}


"""***字典推导式的执行步骤***
创建新作用域：基于当前环境新建一个临时作用域（避免变量污染）。

初始化空字典：准备一个空字典作为结果容器。

遍历可迭代对象：

将每次迭代的元素绑定到变量（如x）。

若有if条件，检查条件是否为True。

若条件满足，将键表达式和值表达式计算结果添加到字典。"""
print({ x: x**2 for x in [1, 2, 3, 4, 5] if x <= 2 })

#Example:Indexing 使指数化

def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which match(k, v) is a true value.

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
# 调用函数并打印结果
result = index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
print(result)
# 输出: {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}