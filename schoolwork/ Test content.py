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


#三角函数
import math
a = input()
b = input()
x = (-int(b)+math.sqrt(2*int(a)*math.sin(math.pi/3)*math.cos(math.pi/3)))/(2*int(a))
print(x)

#表达式求值
import math
x = (-8 + math.sqrt(64-4*5*3))/(2*5)
print(x)

#身份证号校验
Is = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
id = input()
sum = 0
for i in range(17):
    sum = sum + (Is[i]) * int(id[i])
if id[17]=="X":
    if sum % 11 == 2:
        print("身份证号码校验为合法号码！")
    else:
        print("身份证校验位错误!")
elif(sum % 11 + eval(id[17])) % 11 == 1:
    print("身份证号码校验为合法号码！")
else:
    print("身份证校验位错误！")


#3位水仙花数计算
m = int(input())
n = int(input())
result = []
for num in range(m, n+1):
    a, b, c = map(int,str(num))
    if a ** 3 + b ** 3 + c ** 3 == num:
        result.append(str(num))
print (",".join(result))


#同符号数学运算
import math
N = int(input())
abs_N = abs(N)

add_result =int(math.copysign(abs(N)+10, N))
sub_result =int(math.copysign(abs(N)-10, N))
mul_result =int(math.copysign(abs(N)*10 ,N))
print(abs_N, add_result, sub_result, mul_result)


#天天向上的力量III
N = float(input())/1000
dayup = pow(1+N, 365)
daydown = pow(1-N, 365)
ratio = dayup/daydown
print("{:.2f},{:.2f},{:.0f}".format(dayup,daydown,ratio))

#股票交易收益计算
buy, sell, quantity = map(float,input().split)
total_profit = (sell - buy) * quantity
print("f{total.profit:.1f}元")