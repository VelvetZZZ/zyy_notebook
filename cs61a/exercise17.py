#Object-Oriented Programming
#Class Statements
#类的结构拆解（以 `Account` 为例）
def _init_(self, account_holder):
    self.balance = 0
    self.holder = account_holder# 初始化方法 __init__

def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance#存钱方法 deposit

