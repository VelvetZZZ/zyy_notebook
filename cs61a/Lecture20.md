# 🧬 Inheritance（继承）

Inheritance is a method for **relating classes together**.  
继承是一种将多个类联系起来的机制。

---

## 🧠 Why Use Inheritance?

> ✅ 当两个类非常相似，只在细节上略有不同，我们可以使用继承，避免重复代码。

举个例子：
- `Bird` 类：有翅膀，可以飞
- `Penguin` 类：也有翅膀，但不能飞

我们不必把 `Bird` 的所有属性复制粘贴到 `Penguin`，只需要继承即可。

---

## 🧱 基本语法

```python
class 子类名(父类名):
    <子类特有的代码>
```

# Designing for Inheritance

“即使我们覆盖了这个名字（withdraw），也就是说账户将调用这个新的 withdraw，我们仍然可以通过类对象访问原来的 withdraw 并使用它。”

# 🌸 Terminology 专业术语：Inheritance 和 Composition

## 🍀 1. 什么是继承 (Inheritance)
- 表示 is-a 的关系：子类是父类的一种特殊类型。
- 子类自动获得父类的方法和属性（可以重写 override）。

### 示例：
```python
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


class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        # 使用父类的 withdraw 方法，但加上手续费
        return Account.withdraw(self, amount + self.withdraw_fee)
```
✅ 关键点解释：
•	CheckingAccount 是 Account 的子类（is-a 关系）
•	虽然重写了 withdraw 方法，但可以通过 Account.withdraw(...) 访问原方法。
•	self.withdraw(...) 会走子类方法（会递归调用自己 ⚠️），
所以必须用类名 Account.withdraw(...) 来避开这个问题。

## 2. 什么是组合 (Composition)
•	表示 has-a 的关系：一个对象“拥有”另一个对象作为属性。
•	比如银行拥有多个账户，而不是银行是账户。
示例：
```python
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        return sum(acc.balance for acc in self.accounts)
```
✅ 关键点解释：
•	Bank 不是 Account，而是拥有多个 Account。
•	每个 Account 是作为属性存在的。
## 🧠 3. 总结对比（Venn Diagram 风格）

| 项目     | Inheritance（继承）              | Composition（组合）              |
|----------|--------------------------------|--------------------------------|
| 关键词   | is-a（是一个）                    |  has-a（拥有一个）               ｜
| 结构关系 | 子类继承父类                       | 一个类中包含另一个类的实例        |
| 示例     | `CheckingAccount is an Account` | `Bank has a list of Accounts`|
| 优点     | 简洁、可复用逻辑                   | 灵活、低耦合                      |
| 适用场景 | 类型扩展                          | 功能拼装、复杂系统                |

## 🍬 4. Tips 小贴士
	•	✔ 继承：适合一类东西的“特殊化”。
	•	✔ 组合：适合多个类协作完成某个任务。
	•	✔ 若犹豫选哪个？先用组合，再考虑继承

# 🧠 Multiple Inheritance 多重继承学习笔记

## 📌 多重继承简介

在 Python 中，一个类可以同时继承多个父类，这种方式被称为 **Multiple Inheritance（多重继承）**。

它的查找顺序遵循 **方法解析顺序（MRO）**。

---

## 🎯 CleverBank 营销需求场景

CleverBank 想要一种账户类型，具有以下特性：

- 💰 存款收 $2 手续费（SavingsAccount）
- 💸 提款收 $1 手续费（CheckingAccount）
- 🟢 年利率为 1%（CheckingAccount）
- 🎁 开户即送 $1（AsSeenOnTVAccount 自定义）

---

## 🧱 继承结构图
Account
├── CheckingAccount（收 $1 提现费 + 1% 利率）
├── SavingsAccount（收 $2 存款费）
└── AsSeenOnTVAccount（继承以上两者，开户送 $1）