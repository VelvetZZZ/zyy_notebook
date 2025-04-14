#凯撒密码
str = input()
for i in str:
    if'a'<=i<='z':
        print(chr(ord('a')+(ord(i)-ord('a')+3)%26),end='')
    else:
        print(i,end='')

#照猫画虎求阶乘
n = int(input())
sum = 1
for i in range (n, n+1):
    sum *= i
print(sum)

#圆面积的计算
radius = 25
area = 3.1415*radius*radius
print("{:.2f}".format(area))

#说句心里话
name = input("")
word = input("")
print("{},我想对你说,{}".format(name, word))

#世界，你好！
print("世界，你好！")

#Hello World
print("Hello World")

#Hello World II 垂直输出
print("\n".join("Hello World"))

for char in "Hello World":
    print(char)

#2的n次方
n = int(input(""))
print(pow(2, n))

#货币转换
a = input("")
b = eval(input(""))
if eval(a[0:-1])>0:
    if a[-1] in ["$"]:
        c = eval(a[0:-1])*b
        print("{:.2f}¥".format(c))
    elif a[-1] in ["¥"]:
        d = eval(a[0:-1])/b
        print("{:.2f}$".format(d))
    else:
        print("Data error!")

#计算矩形面积
a = eval(input(""))
b = eval(input(""))
print("{:.2f}".format(a*b))

#成绩转换
n = input("")
grade = eval(n)
if 100 >= grade >=60:
    print("pass")
elif 60 > grade >= 0:
    print("fail")
else:
    print("Data error!")

#M与N的数学运算
m = eval(input(""))
n = eval(input(""))

if isinstance(n, int):#isinstance（变量，类型）->内置函数，用来判断“变量是这个类型吗？”
    print(m+n, m*n, pow(m,n), m%n, max(m,n))


#温度转换II
TempStr = input("")

if TempStr[0] in ["C"]:#取首字母判断单位
    F = eval(TempStr[1:]) * 1.8 +32#把输入字符串去掉第一个字母后，剩下的部分当作数字来用，进行计算
    print("F{:.2f}".format(F))#输出要加字母单位——F


else:
    C = (eval(TempStr[1:])-32) / 1.8
    print("C{:.2f}".format(C))#输出字母单位——C

#货币转换I
Currency = input("")
if Currency[0] in ["R","r"]:
    U = eval(Currency[3:])/6.78
    print("USD{:.2f}".format(U))
elif Currency[0] in ["U","u"]:
    R = eval(Currency[3:])*6.78
    print("RMB{:.2f}".format(R))
else:
    print("Data error!")