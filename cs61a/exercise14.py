#Objects
from datetime import date
today = date(2015, 2, 20)
print(today)
freedom = date(2015, 5,12)
print(str(freedom - today))
#通过点表达式访问对象的属性(dot expressions)
print(today.year)
print(today.month)
print(today.strftime('%A %B %d'))

#Strings are objects
s = 'Helllo'
print(s.upper())
print(s.lower())
print(s.swapcase())#交换大小写
#returned a new string based on the old string

#Representing Strings:the ASCII Standard

s = "The python language is a cross platform language."
print(s.find('language', 30))