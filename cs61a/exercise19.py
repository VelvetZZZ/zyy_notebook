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