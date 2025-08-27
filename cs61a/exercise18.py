# Class Attributes 类属性
class Clown:
    nose = 'big and red'  # 定义了一个类 Clown

    def dance():
        return 'No thanks'  # 类方法，返回 'No thanks'

print(Clown.nose)
print(Clown.dance())
print(Clown)


# 正确的 Account 类定义
class Account:
    interest = 0.02  # 类属性

    def __init__(self, account_holder):  # 注意：应是 __init__（两个下划线），而不是 _init_
        self.balance = 0
        self.holder = account_holder


# 放在 if __name__ == "__main__" 中的代码块
if __name__ == "__main__":
    tom_account = Account('Tom')
    jim_account = Account('Jim')

    print(tom_account.interest)  # 0.02
    print(jim_account.interest)  # 0.02

    # Assignment to Attributes（属性赋值）
    class A:
        x = 1

    a = A()
    print(a.x)       # 输出 1（来自类）
    a.x = 2
    print(a.x)       # 输出 2（来自实例）
    print(A.x)       # 仍然是 1（类属性未变）
#By assigning to the class,you don't erase all the special cases!

#Method Calls 方法调用
