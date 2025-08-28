# The Class Statement
## 什么是 class 语句？
```python
class <name>:
    <suite>
```
•	class 是用来定义一个类的关键词。
•	<name> 是你给这个类起的名字（比如 Clown）。
•	<suite> 是类体（缩进块），定义了类的内容——比如变量（属性）或函数（方法）。
💡当你运行 class Clown: 时，Python 会立刻执行 suite 中的代码，并把这些赋值和函数绑定为这个类的属性。

📦 示例拆解
```python
class Clown:
    nose = 'big and red'
    
    def dance():
        return 'No thanks'
```
1.	定义了一个类 Clown。
2.	给这个类添加了两个属性：
nose: 一个类变量，值为 'big and red'
dance(): 一个类方法，返回 'No thanks'

🔍 如何使用这个类？
```python
Clown.nose
# 输出: 'big and red'

Clown.dance()
# 输出: 'No thanks'

Clown
# 输出: <class '__main__.Clown'>
```
说明：
•Clown.nose 是访问类的变量（没有创建实例）。
•Clown.dance() 是直接调用类里的函数。
•Clown 是一个类对象，本质上就是 <class 'Clown'>。
❗ 注意：这个类还没有实例！
  这个例子中我们并没有创建 Clown() 实例对象，只是在直接访问类属性本身。
  这叫做 类属性访问，区别于实例属性

✅ 总结知识点：
概念                               解释
类属性（Class Attribute）        定义在类里、__init__ 外的属性，所有对象共享
实例属性（Instance Attribute）   定义在 __init__ 里，用 self.xxx = ... 赋值，每个对象独立拥有
使用方式                         类属性可以通过类或对象访问：Account.interest 或 tom_account.interest

## Looking Up Attributes by Name（通过名称查找属性）
### ✅ 点表达式是什么？
格式如下：
<表达式>.<名称>
比如：
```python
tom_account.balance
Account.interest
```
### 🔍 查找流程（很关键！）
🟢 第一步：Evaluate the <expression> to the left of the dot…
•先执行点左边的表达式，拿到那个对象。
•例子：tom_account.balance 中，tom_account 会先被求值为一个 Account 实例。
🟢 第二步：<name> is matched against the instance attributes…
•Python 先看这个对象（实例）有没有这个属性。
•如果找到了（例如 balance 是通过 self.balance 赋的），就直接返回。
🟡 第三步（如果实例没有）：If not, <name> is looked up in the class…
•如果这个名字不是实例的属性，Python 会去这个对象的类（class）中找。
•例如 interest 是类属性，不属于某个具体对象。
🔵 第四步：That value is returned unless it is a function…
•如果找到的属性是个普通值（比如数字），就直接返回。
•如果是一个函数（方法），Python 会自动把当前对象作为 self 绑定进去，变成一个“绑定方法”（bound method）。

# getattr 内置函数（获取属性）
🔹 主旨：Python 提供了多种方式来访问对象的属性：
最常见的是通过 点表达式：
tom_account.balance 
也可以使用内置函数 getattr：
getattr(tom_account, 'balance')

```python
>>> hasattr(tom_account, 'deposit')
True
```
hasattr 用来判断某个属性是否存在于对象中。这里检查 tom_account 是否有 deposit 这个方法（存在于类中）。

🔍 总结要点：
	•	getattr(obj, 'name') 和 obj.name 是等价的；
	•	Python 查找属性的方式是一样的：
	1.	先查实例属性
	2.	找不到再查类属性
	•	getattr 和 hasattr 提供了更灵活的方式来动态查找属性；
	•	可能返回的是：
	•	实例的属性，或者
	•	类的属性（包括方法）

# Attribute Assignment 属性赋值语句
## 🟦 Assignment to Attributes（属性赋值）

📌 核心概念：
当你使用点表达式（例如 a.x = value）来进行赋值时，赋值操作修改的是点表达式对象本身的属性，而不是去查找类的定义！

🔹 有两种情况：
	1.	对象是实例（Instance）
	•	比如：tom_account.interest = 0.08
	•	会在 tom_account 实例中新增或覆盖一个名为 interest 的 实例属性。
	•	它 不会 修改 Account 类中原本的 interest 属性！
    2.	对象是类（Class）
	•	比如：Account.interest = 0.04
	•	会直接修改类属性（class attribute）——这个修改会影响到所有没有被实例属性遮蔽的实例。

🧠 重点解释：
	•	tom_account.interest = 0.08 并不会“查找”原来类中有没有这个 interest 属性，而是直接在实例 tom_account 中创建一个新的属性叫 interest。
	•	所以这时候，tom_account.interest 优先访问的是 实例属性，会遮蔽掉类中原本的那个 interest = 0.02。


# map函数的用法
map() 是 Python 的一个内置函数，用于将一个函数应用到一个可迭代对象（如列表、元组、range）中的每个元素上，并返回一个新的迭代器。
```python
map(function, iterable)
```
•function：你想应用的函数（可以是内置函数、自定义函数，或对象的方法）
•iterable：可迭代对象，如列表、元组、range 等
## 为什么map可以用next调用？
因为 map() 返回的是一个 迭代器（iterator），而 next() 函数正是用来从迭代器中取下一个值的。
🔁 什么是迭代器？
在 Python 中，迭代器是一种可以逐个返回元素的对象。每次调用 next()，就会返回一个“下一个”值。

一步一步“惰性地”进行，不会一次性把所有结果都算出来。这种特性叫做：惰性求值（lazy evaluation）

# 🧠 Terminology 专业术语: Attributes, Functions, and Methods

## ✅ 1. Python 中的对象属性（Attributes）

- 所有对象都有属性，属性是 **name-value 对（键值对）**
- 类（Class）是一类对象的**类型**或**分类**
- 类本身也是对象，因此类也可以拥有属性

### 🟡 属性类型分为：
| 属性类型           | 含义                                   |
|--------------------|--------------------------------------|
| Instance Attribute | 实例属性，属于具体对象的属性             |
| Class Attribute    | 类属性，属于类本身的属性，所有对象共享    |

---

## ✅ 2. Python 对象系统（Object System）

- **函数也是对象（Functions are objects）**

- **绑定方法（Bound Methods）也是对象：**
  - 本质上是函数，但第一个参数 `self` 已经自动绑定到了某个实例上
  - 示例：`a.deposit` 是 `deposit(self, amount)` 的绑定版本，`self` 自动是 `a`

- **点表达式（Dot expressions）**
  - 点表达式会返回绑定方法（bound method），如果类属性是函数
  - 示例：  
    ```python
    <instance>.<method_name>
    # 等价于：method(self=instance, ...)
    ```

---

## 🧩 3. 术语总结图示（Venn Diagram）

一个方法（Method）本质是：

- 类属性的一种（属于类）
- 同时也是函数（可以被调用）
- 所以它既是**Class Attribute**，又是**Function**

```text
Terminology:
   ┌─────────────────────┐
   │  Class Attributes    │
   │     ┌────────────┐   │
   │     │  Methods   │◄───── 类属性中是函数的就是方法
   │     └────────────┘   │
   └─────────────────────┘        Functions
            ▲
            └── 既属于类属性，也是函数