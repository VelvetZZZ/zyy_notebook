#Order of Recursive Calls 递归调用的顺序
#The Cascade Function：级联函数
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)#首先打印 n 
        cascade(n//10)#调用的n除以10取整数部分
        print(n)#对cascade的递归调用后再次打印n
print(cascade(5))
print(cascade(12345))
