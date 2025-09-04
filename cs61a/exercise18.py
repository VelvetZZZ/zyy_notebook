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

class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.
    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds avaliable."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
a = Account('Alan')
print(a.deposit(5))
print(a.deposit(5))
print(a.deposit)

b = Account('Ada')
print(b.balance)
print(a.balance)

f = a.deposit
print(f(10))
print(f(10))

m = map(a.deposit, range(10, 20))#将 range(10, 20) 中的每个数依次作为 amount 传入 a.deposit(amount) 中。
print(a.balance)#map函数的用法见md
print(next(m))
print(next(m))

#Bound Methods
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing {amount} to", self)
        return self.balance
f = a.deposit  # 👈 这是一个 bound method
a = Account()
print(type(Account.deposit))
print(type(a.deposit))  # 而不是 tom_account.deposit
print(Account.deposit(a, 1001))
print(a.deposit(1007))

