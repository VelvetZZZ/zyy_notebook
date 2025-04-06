#List列表（赋值语句即可调用）  
#odds奇数 (元素选择表达式：gives you a list->you have to evaluate the index索引)

odds=[41, 43, 47, 49]
print(odds[0])
print(odds[1])
print(odds[2])
print(odds[3])
print(len(odds))#len(内置函数）元素数量

#Lists两种调用形式
digits = [1, 8, 2, 8]
digits = [2//2, 2+2+2+2, 2, 2*2*2*2]

#通过索引找到一个元素（元素选择法/调用getitem函数）

print(digits[3])

from operator import getitem
print(getitem(digits, 3))

#Concatenation 连接/合并 and repetition（也有两种方法）

print([2, 7] + digits * 2 )#乘以列表两次->将元素复制两次，并将元素加到列表末尾

from operator import add, mul
print(add([2, 7], mul(digits, 2)))

#Nested list 嵌套列表
pairs = [[10, 20], [30, 40]]
print(pairs[1])
print(pairs[1][0])

#Containers

digits = [1, 8, 2, 8]
print(1 in digits)#in is an operator运算符
print(5 in digits)

print(5 not in digits)
print(not(5 in digits))

print('1'==1)#字符串1不是整数1

print([1, 8]in digits)#寻找独立元素[1, 8]是否在列表里->False

print([1, 8]in [3, [1, 8], 4])#寻找独立元素[1, 8]是否在列表里->True
"""  in 是一个简单的运算符，
    它不会在结构中搜索任何与之匹配的内容，
    只是逐个元素地检查是否等于你要查找的元素"""

#For Statements（a way of iterating over sequences迭代序列)
"""def count(s, value):
      Count the number of times that value in sequence s
       统计值在序列S中出现的次数
    total, index = 0, 0
    while index < len(s):
        element = s[index]

        if element == value:
            total += 1
        index =+ 1
    return total
print(count([1, 2, 1, 2, 1], 1))"""


#for statement采用
def count(s, value):
    """Count the number of times that value in sequence s
       统计值在序列S中出现的次数"""
    total= 0
    for element in s:
        if element == value:
            total += 1
    return total
print(count([1, 2, 1, 2, 1], 1))

#for结构
for char in "hello":
    print(char.upper())

#Sequence Unpacking in For Statements（for 循环中的序列解包）

pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count = same_count + 1

same_count
# 输出: 2

#Range序列
print(list(range(-2, 2)))#List constructor
print(list(range(4)))#Range with a 0 starting value

print(range(5, 8))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total
print(sum_below(5))

def cheer():
    for _ in range(3):
        print("加油！")
print(cheer())


#List comprehension 列表理解
odds = [1, 3, 5, 7, 9]
print([x+1 for x in odds])
print([x for x  in odds if 25 % x == 0])#list comprehension允许我们选择想要保留的列表部分
