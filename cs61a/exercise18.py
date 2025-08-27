#Class Attributes 类属性
class Clown:
    nose = 'big and red'#定义了一个类 Clown。

    def dance():
        return 'No thanks'#给这个类添加了两个属性：nose: 一个类变量，值为 'big and red'; dance(): 一个类方法，返回 'No thanks'。
print(Clown.nose)
print(Clown.dance())
print(Clown)
    

class Account:
    interest = 0.02 # A class attribute
    def _init_(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    # Additional methods would be defined here
tom_account = Account('Tom')
jim_account = Account('Jim')
print(tom_account.interest)#0.02
print(jim_account.interest)#0.02
# interest 是类级别共享的，不是每个对象自己独立拥有的。