# 主题：Objects（对象）

## 什么是对象（Objects）？
	•	Objects represent information
→ 对象是用来“表示信息”的。比如，一个“学生”对象可以表示学生的姓名、年龄、成绩等信息。
	•	They consist of data and behavior, bundled together to create abstractions
→ 对象包含 数据（data） 和 行为（behavior），它们被“打包”在一起。这种方式叫做 抽象（abstraction） —— 用简单的方式表示复杂的事物。
✅ 举例：你可以用一个“猫”对象来表示一只猫，它的数据是“名字、年龄、颜色”，它的行为可能是“喵喵叫、抓老鼠”。

⸻

## 对象可以表示什么？
	•	Objects can represent things, but also properties, interactions, & processes
→ 它不仅能代表“东西”（比如猫、车、人），还能表示“属性、相互作用、过程”。这比传统的函数更强大。

⸻

#  什么是类（Class）？
	•	A type of object is called a class; classes are first-class values in Python
→ 类是一种“对象的模板”，用来创建多个类似的对象。比如有一个 Student 类，你可以用它创建很多学生对象。
在 Python 中，类本身也是一个对象（也就是说，类也是值，也可以传递、赋值）。

⸻

#  面向对象编程（Object-Oriented Programming, OOP）
	•	A metaphor for organizing large programs
→ 面向对象编程是一种组织大型程序的方法。它就像你在写小说时，用“角色”来推动故事一样，你用“对象”来组织程序。
	•	Special syntax that can improve the composition of programs
→ OOP 有专门的语法，让你写出结构更清晰、更容易维护的代码。

⸻

#  Python 的对象模型
	•	In Python, every value is an object
→ 在 Python 里，一切皆对象！（包括整数、字符串、函数、模块……）
	•	All objects have attributes
→ 每个对象都有“属性”，比如字符串对象有 .upper() 方法，列表对象有 .append() 方法。
	•	A lot of data manipulation happens through object methods
→ 数据操作主要通过对象的方法（method）来实现。方法就像对象的“功能”。
	•	Functions do one thing; objects do many related things
→ 函数只做一件事，但对象可以包含多个相关的功能。例如，一个“车”对象可以有“启动、加速、刹车”等方法。

⸻

📝 总结笔记（适合记在本子上）
	1.	对象（Object） = 数据 + 行为，构建程序的基本单位。
	2.	类（Class） = 创建对象的模板。
	3.	面向对象编程（OOP）：更适合构建大型项目的方式，结构清晰。
	4.	在 Python 中，所有的值都是对象（包括函数、数字、字符串等）。
	5.	对象方法 = 操作数据的工具（如 str.upper()，list.append()）。
	6.	区别函数和对象：
	•	函数：单一功能；
	•	对象：多个相关功能组合在一起。



# 🧵 Python 字符串编码与 Unicode 标准笔记



## 📘 什么是 Unicode？

Unicode 是一个全球统一的字符编码系统，为每一个字符（不论语言、符号）分配一个唯一编号（称为“码位”）。

---

## 📦 Unicode 特点

- **109,000+ 字符**
- **93 套文字系统（Scripts）**
- 每个字符有 **属性**（如是否为大写字母）
- 支持 **双向显示**（例如阿拉伯语从右到左）
- 每个字符有 **唯一标准英文名称**

---

## 🎯 示例字符（幻灯片中的例子）

| 编码（码位） | 字符 | 名称 |
|-------------|------|------|
| `U+0058`    | X    | LATIN CAPITAL LETTER X |
| `U+263A`    | ☺️   | WHITE SMILING FACE     |
| `U+2639`    | ☹️   | WHITE FROWNING FACE    |

---

## 🐍 Python 中的字符串和编码

Python 的字符串（`str` 类型）默认使用 Unicode 编码，可以自然地支持中文、emoji 等各种字符。

### 常用函数

```python
ord('你')     # 返回 Unicode 编码：20320
chr(20320)   # 返回字符：'你'
hex(ord('你'))  # 返回十六进制字符串：'0x4f60'







当然可以！让我以“伯克利大学的计算机科学教授”的视角，为你逐句讲解这页幻灯片的深层含义，并提供清晰易懂的 Markdown 学习笔记，特别适合 Python 初学者理解“对象、变量名、变异（mutation）和可变类型（mutable types）”等关键概念。

⸻

🧑‍🏫 幻灯片标题：Some Objects Can Change

⸻

💡 主旨：

Python 中的一些对象是可以改变的（mutable），改变的是对象本身的状态，而不是变量的名字。

⸻

🎯 核心概念解释：

⸻

🔁 对象的状态可以改变

“The same object can change in value throughout the course of computation.”

	•	在 Python 中，对象（比如列表、字典）可以在程序运行的过程中被修改。
	•	即使变量名没有变，背后的对象值也可能改变。

⸻

👩 变量名指向对象（名字绑定）

图中：

jessica → 👵 OLDER WOMAN
same_person → 👵 OLDER WOMAN

	•	jessica 和 same_person 是两个名字，指向同一个对象。
	•	这个对象是一个 emoji 表示的“老人” 👵（其实这也是一个 Unicode 字符）。

⸻

🔄 变异（Mutation）

“All names that refer to the same object are affected by a mutation”

	•	如果我们修改这个对象（假设它是可变的），所有绑定到这个对象的名字都会看到变化。
	•	这叫做变异（mutation）。

⸻

🔒 可变 vs 不可变对象

“Only objects of mutable types can change: lists & dictionaries”

类型	是否可变	示例
列表 list	✅ 可变	a = [1, 2]; a[0] = 10
字典 dict	✅ 可变	d = {'x': 1}; d['x'] = 42
字符串 str	❌ 不可变	s = "hi"; s[0] = 'H' ❌ 报错
元组 tuple	❌ 不可变	t = (1, 2, 3)



⸻

📘 举个真实例子：

a = [1, 2, 3]
b = a           # b 和 a 指向同一个列表对象

a[0] = 99       # 修改了列表内容

print(b)        # 输出：[99, 2, 3] ← b 也看到变化了

说明 a 和 b 是两个名字，但都绑定到同一个可变对象。

⸻

📝 Markdown 学习笔记版本

# 🧠 Python 对象的可变性（mutability）笔记

## 🎯 本节目标

理解变量名和对象的关系，以及哪些对象是可以“变”的。

---

## 🔗 变量名 vs 对象

在 Python 中：

- **变量名** 是标签（标签贴在哪，值就在哪）
- **对象** 是真正的数据
- 多个变量名可以指向同一个对象

---

## 🌀 对象的“变”（mutation）

```python
a = [1, 2, 3]
b = a

a[0] = 99

print(b)  # 输出：[99, 2, 3]

	•	a 和 b 是两个名字，但引用的是同一个列表对象
	•	列表是可变的，所以修改了一个，另一个也看到变了

⸻

🔒 可变类型 vs 不可变类型

类型	是否可变	  示例
list	✅ 是	   a[0] = 10
dict	✅ 是	   d['key'] = 1
set	    ✅ 是	   s.add(2)
str（字符串）❌ 否	 s[0] = 'H' ❌ 报错
tuple（元组）❌ 否	 t = (1, 2)
int、float	❌ 否	x = 5; x = 6 是重新绑定



⸻

👀 图示总结（来自幻灯片）
	•	jessica 和 same_person 指向一个“👵”角色（emoji）
	•	改变这个对象的状态 → 所有指向它的名字都会看到变化
	•	这个 emoji 是一个 Unicode 字符（也是对象）

⸻

✅ 小结
	•	Python 中的变量名是引用（reference）
	•	修改对象内容会影响所有引用它的变量名
	•	只有 可变类型（mutable） 可以在原地被改变（如 list、dict）



### Python 可变值与持久局部状态讲解笔记

---

#### **1. 核心概念**
- **可变对象（Mutable Objects）**：例如列表（`list`），其内容可以被修改，但变量引用的对象本身不变。
- **闭包（Closure）**：内部函数可以访问并记住其外部函数的作用域，即使外部函数已执行完毕。
- **持久状态（Persistent State）**：函数在多次调用之间能“记住”之前的状态。

---

#### **2. 代码解析**
```python
def make_withdraw_list(balance):
    b = [balance]  # 用列表保存余额（可变对象）
    def withdraw(amount):
        if amount > b[0]:
            return "Insufficient funds"
        b[0] -= amount  # 修改列表元素的值
        return b[0]
    return withdraw  # 返回闭包函数

# 使用示例
withdraw = make_withdraw_list(100)  # 初始余额100
print(withdraw(25))  # 输出75
print(withdraw(30))  # 输出45
```

---

#### **3. 关键机制**
##### **为什么用列表？**
- **不可变对象的问题**：若直接使用整数（不可变），在内部函数中修改会触发`UnboundLocalError`（Python认为它是局部变量）。
- **可变对象的优势**：列表内容可修改，且闭包中的函数持有对同一列表的引用，状态得以持久化。

##### **闭包的作用**
- `withdraw`函数“记住”了父函数`make_withdraw_list`中的列表`b`。
- 每次调用`withdraw`时，修改的是`b[0]`的值，而非重新赋值变量`b`。

##### **状态独立性**
```python
wd1 = make_withdraw_list(100)  # wd1维护自己的余额列表
wd2 = make_withdraw_list(200)  # wd2的余额独立于wd1
wd1(25)  # 75
wd2(25)  # 175
```
- 每次调用`make_withdraw_list`会生成新的闭包，每个闭包拥有独立的`b`列表。

---

#### **4. 框架（作用域）分析**
- **全局框架（Global Frame）**：包含`make_withdraw_list`和`withdraw`（函数对象）。
- **f1框架**：调用`make_withdraw_list(100)`时创建，包含列表`b = [100]`。
- **f2框架**：调用`withdraw(25)`时创建，处理参数`amount=25`，并修改`b[0]`的值。

---

#### **5. 对比：使用类实现相同功能**
```python
class Withdraw:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

# 使用类
account = Withdraw(100)
account.withdraw(25)  # 75
```
- 闭包是一种轻量级替代方案，适合简单场景；类更适用于复杂状态管理。

---

#### **6. 常见疑问解答**
- **为何不用`nonlocal`关键字？**  
  `nonlocal`（Python 3+）允许修改外部作用域的不可变变量，但此示例展示了通过可变对象实现的传统方法。
- **如果`b`是整数会怎样？**  
  会报错，因为内部函数尝试修改外部作用域的不可变变量（需用`nonlocal`声明）。

---

#### **7. 总结**
- **核心技巧**：通过闭包和可变对象（如列表）实现函数的状态持久化。
- **适用场景**：简单状态管理，无需定义类。
- **扩展思考**：闭包在装饰器（Decorator）、函数式编程中的应用。

