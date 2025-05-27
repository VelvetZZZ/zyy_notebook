#Iterators
s =[3, 4, 5]
t = iter(s)
print(next(t))
print(next(t))

u = iter(s)
print(next(u))
print(next(t))
print(next(u))#iterator is independent

s = [[1, 2], 3, 4, 5]
#If you print'next'here,you'll get a TypeError:'list' object is not an iterator
t = iter(s)
print(next(t))
print(next(t))
print(list(t))#We already used up the list[1, 2]&number3
#If you print'next(t)' here, Python will raise a stop iteration.This how you tell you're at the end.


#Dictionary Iteration
d = {'one': 1, 'two': 2, 'three': 3}
d['zero'] = 0#添加一个新的键值对（key-value pairs）
#获取键视图的迭代器
k = iter(d.keys())#or iter(d)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
# >>> next(k)  # 如果再调用一次，会引发 StopIteration
# 获取值视图的迭代器
v = iter(d.values())
print(next(v))
print(next(v))
print(next(v))
print(next(v))
#与键类似，d.values() 提供值的视图，iter() 创建迭代器 v。next(v) 按照对应键的插入顺序返回值。
# 获取项视图的迭代器
i = iter(d.items())
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#***每个项是一个元组 (key, value)***


#使用for循环会更简洁
d = {'one': 1, 'two':2, 'three': 3}
d['zero'] = 0

print("Keys:")
for key in d :
    print(key)
print("\nValues:")#\n 是一个转义字符，代表一个换行符。所以这行代码会先换一行，然后再打印文本 "Values:"
for value in d.values():
    print(value)

print("\nItems:")
for key, value in d.items():#元组解包 (tuple unpacking)
    print(f"Key: {key}, Value: {value}")

#iterator is invalid 迭代器无效的情况
'''在迭代一个字典的过程中，不应该改变该字典的大小（即添加或删除元素）
如果你这么做了,Python 通常会抛出一个 RuntimeError'''
d = {'one': 1, 'two': 2}#字典 d 的大小是 2 (因为它包含两个元素)。
k = iter(d)
print(next(k))

d['zero'] = 0#向字典 d 中添加一个新的键值对：'zero': 0,字典 d 的大小从 2 变成了 3
#print(next(k))
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration"""

print(d)
k = iter(d)
print(next(k))
print(next(k))
d['zero'] = 5
print(next(k))
#如果改变的是字典中已存在键的值，而不是添加或删除键（即不改变字典的大小），那么迭代通常可以继续（尽管这仍然可能导致逻辑上的困惑，但不会直接触发 RuntimeError）。(对键、值、项都一样)

#For Statements
r = range(3, 6)
ri = iter(r)
for i in ri:
    print(i)

for i in ri:
    print(i)#see nothing

for i in r:
    print(i)
for i in r:
    print(i)#for statement->able to go through the entire contents from beginning to end without worrying about changing.

#Built-In Iterator Functions迭代的内建函数 
bcd = ['b', 'c', 'd']
print([x.upper() for x in bcd])

map(lambda x: x.upper(), bcd)
m = map(lambda x: x.upper(), bcd)
print(next(m))
print(next(m))
print(next(m))
