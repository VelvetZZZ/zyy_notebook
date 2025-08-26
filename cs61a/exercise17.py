#Object-Oriented Programming
#Class Statements
#类的结构拆解（以 `Account` 为例）
def _init_(self, account_holder):
    self.balance = 0
    self.holder = account_holder# 初始化方法 __init__

def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance#存钱方法 deposit

#创建并使用对象的示例
a = Account('John')      # 创建账户 a，持有人是 John
a.holder                 # 输出账户持有人
# 'John'

a.balance                # 查询账户余额
# 0

a.deposit(15)            # 存入 15 元
# 15

a.withdraw(10)           # 取出 10 元
# 5

a.withdraw(10)           # 再次取出 10 元，余额不够
# 'Insufficient funds'

