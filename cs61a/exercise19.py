# Inheritance
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

a = Animal()
a.speak()  # print: Some sound
d = Dog()
d.speak()   # print: Woof!
#Dog 继承自 Animal，但它重写（override）了 speak 方法。

#定义父类
class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing {amount} to {self.name}")
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawing {amount} from {self.name}")
        return self.balance
#定义子类
class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
ch = CheckingAccount('Tom')
ch.interest
ch.deposit(20)
ch.withdraw(5)

a = Account('John')
b = CheckingAccount('Jack')
print(a)
print(b)
a.balance
b.balance
a.deposit(100)
b.deposit(100)
a.withdraw(10)
b.withdraw(10)

#Object-Oriented Design

class Account:
    def withdraw(self, amount):
        print(f"[Account] Withdrawing {amount}")#普通的取钱方法


class CheckingAccount(Account):
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)#自己定义的新方法，加手续费
ch = CheckingAccount()
ch.withdraw(5)
#子类可以写一个新的方法，名字和父类一样，这叫 override（重写）。
#但是 父类的方法还在，你可以通过 父类.方法(self, ...) 的方式来访问它！

#Inheritance and Composition 何时继承，何时组合

#Composition
class Bank:
    """A bank *has* a accounts.
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):
        self.accounts = []
    def open_accounts(self, holder, amount, kind = Account):
        account = kind(holder)
        account.deposit(amount)
        self. accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fall(self):
        return len(self.accounts) > 1
    
    #Attributes Lookup Practice
class A:
    z = -1
    def f(self, x):
        return B(x - 1)
    
class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)

class C(B):
    def f(self, x):
        return x
    
a = A()
b = B(1)
c = C(2)   













#Multiple Inheritance 多重继承
# 父类 Account：基础账户类
class Account:
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"[Account] Depositing {amount}, new balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"[Account] Withdrawing {amount}, new balance: {self.balance}")
        return self.balance


# 子类 CheckingAccount：提款收 $1 手续费
class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        print(f"[CheckingAccount] Withdrawing with $1 fee")
        return Account.withdraw(self, amount + self.withdraw_fee)


# 子类 SavingsAccount：存款收 $2 手续费
class SavingsAccount(Account):
    deposit_fee = 2

    def deposit(self, amount):
        print(f"[SavingsAccount] Depositing with $2 fee")
        return Account.deposit(self, amount - self.deposit_fee)


# 多重继承类 AsSeenOnTVAccount
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # 免费送你一美元
        print(f"[AsSeenOnTVAccount] Opened account for {self.holder}, initial balance: {self.balance}")


# 测试代码
a = AsSeenOnTVAccount("Zhang Yuyues")

# 存款 $10（测试 deposit）
a.deposit(10)  # 会使用 CheckingAccount 中的 deposit 吗？没有定义 → 向后查找 MRO → SavingsAccount.deposit()

# 提款 $5（测试 withdraw）
a.withdraw(5)  # 会使用 CheckingAccount 中的 withdraw

# 查看最终余额
print(f"Final balance: {a.balance}")