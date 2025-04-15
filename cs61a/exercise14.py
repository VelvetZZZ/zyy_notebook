#Objects
from datetime import date
today = date(2015, 2, 20)
print(today)
freedom = date(2015, 5,12)
print(str(freedom - today))
#通过点表达式访问对象的属性(dot expressions)（special syntax）
print(today.year)
print(today.month)
print(today.strftime('%A %B %d'))#格式化日期时间string format time

#Strings are objects
s = 'Helllo'
print(s.upper())
print(s.lower())
print(s.swapcase())#交换大小写
#returned a new string based on the old string

#Representing Strings:the ASCII Standard
a ='A'
print(ord(a))#ord->返回单个字符的 Unicode 编码（码位）
print(hex(ord(a)))#hex->将一个整数转换成十六进制字符串表示形式('0x'开头的十六进制）
print('\n\n\n')
print('\a\a\a')#响铃字符（bell character）


s = "The python language is a cross platform language."
print(s.find('language', 30))

#Representing Strings:the Unicode Standard
from unicodedata import name, lookup
print(name('A'))
print(name('a'))
print(lookup('WHITE SMILING FACE'))
print(lookup('SNOWMAN'))
print(lookup('BABY'))

print(lookup('BABY').encode())
print('A'.encode())


#Mutation Operations（突变操作）：Some Objects Can Change
#list
suits = ['coin', 'string', 'myriad']
original_suits = suits
print(suits.pop())
suits.remove('string')
print(suits)
suits.append('cup')#将一个元素加到列表末尾
suits.extend(['sword', 'club'])#把一个可迭代的对象的每个元素都添加到列表中
print(suits)
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']

print(suits)
print(original_suits)#同一个对象的两个不同名称

#dict
numerals = {'I': 1, 'V': 5, 'X':10}
print(numerals['X'])
numerals['X'] = 11
print(numerals['X'])
print(numerals)

numerals['L'] = 50
print(numerals)
print(numerals['L'])

numerals.pop('X')#移除一个键值对
print(numerals)

def mystery(s):
    s.pop()#remove the last element
    s.pop()
    return s#***
four = [1, 2, 3, 4]
print(mystery(four))

def mystery(s):
    s[2:] = []#Remove evey element after index 2

four = [1, 2, 3, 4]
print(len(four))
def another_mystery(s):
    four.pop()
    four.pop()
    return s
another_mystery(s)
print(len(four))


#Tuples元组是不可变序列（immutable）
(3, 4, 5, 6)
3, 4, 5, 6#Anything separated by commas逗号分隔的任何东西都是元组

print(tuple())
print(tuple([3, 4, 5]))

print((3, 4) + (5, 6))
print(5 in (3, 4, 5))
#tuples can be used as key in dict
{(1, 2): 3}

#A immutable sequence may still change if it contains a mutable value as an element
s = ([1, 2], 3)
#s[0] = 4 ->ERROR
s[0][0] = 4
print(s)


#Identity Operators身份运算符：is / is not(内存地址相同/不相同)；==（值相等）

print([10] == [10])

a = [10]
b = [10]
print(a == b)
print(a is b)

a.extend([20, 30])
print(a)

#Mutable Default Arguments are Dangerous
def f(s=[]):
      s.append(3)
      return len(s)
print(f())
print(f())
print(f())#“共享默认列表”



#A Function with Behavior That Varies Over Time
#Persistent Local State

def make_withdraw_list(balance):
     b = [balance]
     def withdraw(amount):
          if amount > b[0]:
             return 'Insufficient funds'
          b[0] = b[0] - amount
          return b[0]
     return withdraw
          
withdraw = make_withdraw_list(100)

print(withdraw(25))
