# 🧠 Python 对象的字符串表示（String Representations）

在 Python 中，对象可以通过字符串形式来表达自己的含义。这种表达不仅是为了输出信息，也方便人类阅读和调试程序。

## 🔍 为什么字符串表示很重要？

- 字符串是连接**程序与人类**的桥梁。
- 一个对象如果能正确地表现自己，会使得调试与阅读变得更加清晰。

## ✌️ 两种字符串表示形式

| 表示方式 | 方法名        | 适用对象      | 说明                  |
|----------|---------------|---------------|-----------------------|
| `str()`  | `__str__()`   | 人类用户       | 面向用户的友好描述     |
| `repr()` | `__repr__()`  | 开发者 & 解释器 | 面向开发者的精确表达   |

---

## 🧪 示例代码：

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"A dog named {self.name}"

    def __repr__(self):
        return f"Dog('{self.name}')"

d = Dog("Choco")

print(str(d))   # 输出: A dog named Choco
print(repr(d))  # 输出: Dog('Choco')
```
场景           使用方法
print(obj)    调用 str() （更美观）
obj（解释器中） 调用 repr() （更精确）


# The repr String for an Object（repr()字符串表示）
## 🔹 什么是 repr()？
repr(object) 返回一个 字符串，这个字符串应当尽可能是一个 可以被 eval() 执行并还原出原对象的 Python 表达式。

```python
eval(repr(obj)) == obj   # 通常成立
```
## 🔍 用途
•	调试为主，用于精确、正式地表示对象。
•	交互式解释器（比如直接运行 Python 命令行）中默认用 repr() 显示结果。

## ⚠️ 注意事项
•	并不是所有对象都有一个“能被 eval 还原”的 repr 表达式。
例如内置函数：
```python
>>> repr(min)
'<built-in function min>'
```
这是 Python 能表示 min 的方法，但并不能用 eval() 来还原出这个对象。

### 🧠什么是eval()函数？
eval() 是 Python 的一个内置函数，全名是：
```python
eval(expression_string)
```
它的作用是：
把一个“字符串表达式”当成 Python 代码执行，并返回结果。

### 🧠那 repr() 和它有什么关系？
repr() 的职责就是：返回一个字符串表达式，这个表达式“理想情况下”可以交给 eval() 来还原出原对象。
```python
eval(repr(x)) == x  ✅  # 通常成立
```
###  🧠print(repr(12e12)) 是什么意思？
1.	12e12 是科学计数法，等于 12 * 10^12，也就是 12000000000000.0。
2.	repr(12e12) 生成这个数字的“准确字符串表示”：
* Python 用 e（或 E）来表示“×10 的多少次方”

###  环境输出差异解释
•print(str(obj))：显示字符串内容，不带引号
•str(obj) 直接在 解释器里敲，可能会通过 repr() 自动显示，带引号
•repr(str(obj))：会明确显示引号，表示是字符串本身。


# ❓ VS Code 中为什么必须用 `print()` 才能看到输出？

---

## 🧠 1. 区别在于「环境」

| 环境              | 输出行为                                  |
|-------------------|-------------------------------------------|
| Python 解释器 / REPL（如终端直接运行 `python`） | 自动调用 `repr()` 显示表达式的值 |
| VS Code / 脚本运行（`.py` 文件）             | **不会**自动输出表达式结果，必须使用 `print()` |

---

## 💬 举例说明

在 Python 解释器中：

```python
>>> 1 + 1
2
```
✅ 小结
•	🖥 VS Code / 脚本运行模式：要用 print() 才能看到结果
•	🐍 解释器 / REPL 模式：可以省略 print()，自动帮你展示最后一个表达式的结果


# 🎯 `repr()` 与 `eval()` 的“互逆”关系：

- `repr(obj)` 生成**合法 Python 字符串**，可被 `eval()` 还原。
- 多次 `repr()` 会不断“包装”字符串，加上转义字符。
- 多次 `eval()` 就像“拆套娃”，逐层还原出原始对象。

### 🚫 错误用法：`eval(s)` 不总是合法

- 如果 `s` 是 `"Hello, World"`（没有引号包住的字符串），就不是合法 Python 表达式。
- 所以 `eval(s)` 会报错 —— NameError。

### 🧪 示例：
```python
s = "Hello, World"
repr(s)            # => "'Hello, World'"
eval(repr(s))      # => 'Hello, World'
repr(repr(repr(s)))  # => "'\\'\\'Hello, World\\'\\''"
eval(eval(eval(...)))  # 成功还原原始字符串
```
🧠 讲这个的目的是什么？
核心思想：repr() 是为了生成一个合法的、可以用 eval() 还原对象的字符串表示形式。

老师通过这个例子要说明：
•	repr() 一次，是把对象 → 字符串
•	eval() 一次，是把字符串 → 对象
•	多次 repr()，你其实是把“字符串的字符串的字符串……”包装起来
•	只有 eval() 对应“拆包”次数够多，你才能最终还原最初的对象


### F-string表达式的副作用
在 f-string 中，花括号 {} 中的表达式是从左往右依次求值的：
```python
f'{expr1} {expr2} {expr3}'
```

- 在 f-string 中，花括号 `{}` 中的每个表达式都会被求值。
- 如果表达式本身具有副作用（如 list.pop() 会改变列表），那么会影响后续表达式的计算结果。

### 🧪 示例：

```python
s = [9, 8, 7]
f"Result: {s.pop()} {s.pop()} {s}"  # -> 'Result: 7 8 [9]'
```


# 📌 Python 多态函数与双下划线方法（Magic Methods）

## ✅ 什么是 Polymorphic Function？

- 多态函数是指能作用于多种不同类型对象的函数。
- Python 中 `str()` 和 `repr()` 就是典型例子。

**多态函数（Polymorphic Function）** 并不是某一种特定的函数，而是：
> 一类可以作用于不同类型对象，并根据对象类型表现出不同行为的函数。
### 🌟 举例说明

```python
str(123)          # 输出: '123' （整数）
str(3.14)         # 输出: '3.14' （浮点数）
str([1, 2, 3])    # 输出: '[1, 2, 3]' （列表）
str({'a': 1})     # 输出: "{'a': 1}" （字典）
```

## 🎯 str() 和 repr() 的本质

| 函数调用     | 实际方法调用      |
|--------------|-------------------|
| `str(obj)`   | `obj.__str__()`   |
| `repr(obj)`  | `obj.__repr__()`  |

---

## 📌 双下划线方法的常见例子（Magic Methods）

| 方法名       | 对应功能                                     |
|--------------|----------------------------------------------|
| `__str__()`  | 字符串表现，用于人类阅读                      |
| `__repr__()` | 开发者调试用，可被 `eval` 解析               |
| `__len__()`  | 实现 `len(obj)`                              |
| `__add__()`  | 实现 `a + b` 运算                            |
| `__eq__()`   | 实现 `a == b` 判断                           |
| `__bool__()` | 实现 `bool(obj)`，将对象转换为 True 或 False |
| `__float__()`| 实现 `float(obj)`，将对象转换为浮点数        |

---

## 🧪 示例

```python
from fractions import Fraction

half = Fraction(1, 2)

print(str(half))        # 1/2
print(repr(half))       # Fraction(1, 2)

# 等价于：
print(half.__str__())   # 1/2
print(half.__repr__())  # Fraction(1, 2
```


# 🐍 Python 多态函数与 `self` 参数使用笔记

## ✅ 什么是 `self`？
- `self` 是类中实例方法的第一个参数，**代表当前对象自身**。
- 当你通过对象调用方法时，Python 会自动把该对象作为第一个参数传给方法。
- 尽管可以使用别的名字（比如 `this`），但 **Python 社区习惯用 `self`**。

---

## 🌟 哪些情况需要 `self`？
- **类的实例方法**中定义时必须有 `self`，因为这些方法要访问对象的属性或其他方法。

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
d = Dog("Fido")
d.bark()  # 输出: Fido says woof!
```
## 🚫 哪些情况不需要 self？
类型      是否需要 self      说明
实例方法   ✅ 是             操作对象自身的数据
静态方法   ❌ 否             类中定义但不访问对象/类数据，像普通函数
类方法（@classmethod）❌（使用 cls）操作类本身，而非实例对象

```python
class MathTool:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def description(cls):
        return f"This is {cls.__name__}"
```

## 🎯 self 的使用总结

| 使用位置     | 是否写 `self` | 原因说明                                 |
|--------------|-------------|------------------------------------------|
| 方法定义时   | ✅ 必须写上     | 告诉 Python 这个方法绑定到对象           |
| 方法调用时   | ❌ 不需要       | Python 会自动把对象作为 `self` 传入       |

## 📌 self 是怎么工作的？
```python
class A:
    def show(self):
        print("Hi")

a = A()
a.show()         # 自动转为 A.show(a)
A.show(a)        # 等效写法
```
## 📚 额外提示
__init__ 是类的构造函数，第一个参数也必须是 self。!!!
self 可以用来动态添加属性：self.age = 20


# 🧠 Implementing repr and str

⸻

## 📌 repr 的行为（Behavior of repr）

repr(x) 的行为比直接调用 x.__repr__() 更复杂。

	•	✅ 实例上的 __repr__ 属性会被忽略。
	•	✅ Python 只查找类属性（class attribute）里的 __repr__ 方法。

❓如何模拟 repr(x) 的内部行为？

以下是几种实现方式的对比：

标记	实现方式	是否正确	说明
👆	def repr(x): return x.__repr__(x)	❌	多传了一个参数，__repr__ 只接受一个 self 参数
✌️	def repr(x): return x.__repr__()	⚠️	有可能调用的是实例属性，而不是类属性
✅	def repr(x): return type(x).__repr__(x)	✅	完整模拟 Python 行为，从类属性中查找并传入实例
✋	def repr(x): return type(x).__repr__()	❌	缺少参数，类方法需要传入实例
🖐	def repr(x): return super(x).__repr__()	❌	错误语义，super(x) 只能在类定义内部使用


⸻

## 📌 str 的行为（Behavior of str）

str(x) 的行为类似但略有不同：

	•	✅ 也会 忽略实例上的 __str__ 属性
	•	✅ 如果 没有定义 __str__，会退而调用 repr(x)

⸻

📎 总结 Summary（中英对照）

函数行为	英文解释	中文解释
repr(x)	Only looks for __repr__ on class, not on instance	只查类的 __repr__，忽略实例绑定的 __repr__ 方法
str(x)	Same as repr(x) if no __str__ is defined	如果类没有 __str__，就回退使用 repr(x) 的结果
实现 repr(x)	type(x).__repr__(x)	正确模拟方式是从类中查找并调用，传入实例本身为参数


⸻

🧑‍🏫 推荐用法：永远用 type(x).__repr__(x) 来实现自己的 repr()，确保行为和 Python 内部一致。

# 🧠 什么是接口（Interface）?

英文定义：
An interface is a set of methods that a class agrees to implement so that it can interact with other parts of the code in a predictable way.

中文解释：
接口是类中约定要实现的一组方法，这些方法让对象在和其他代码交互时具有一致性和可替代性。

## 接口的本质不是语法，而是一种 约定。只要类实现了某些特殊名字的方法（像 __str__, __repr__），Python 内置函数就知道该怎么处理这个对象：
	•	str(obj) ➜ 自动调用 obj.__str__()
	•	repr(obj) ➜ 自动调用 obj.__repr__()

你只要“遵守约定”去实现这些方法，Python 就会在适当的时候自动调用它们，这就形成了一个“接口”。



# 🧮 Python Ratio 类详解笔记

本笔记根据伯克利 CS61A 课程中的 Ratio 类示例，结合截图内容进行讲解，特别聚焦在两个重要策略：类型分派（Type Dispatching）和 类型强制转换（Type Coercion）。

⸻

📌 代码示例：Ratio 类
```python
class Ratio:
    def __init__(self, n, d):
        self.number = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.number, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.number, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.number + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.number * other.denom + self.denom * other.number
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__

    def __float__(self):
        return self.number / self.denom


def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n - d)
    return n

```
⸻

🎯 设计目的：兼容多种加法操作

通过重载 __add__ 和 __float__ 方法，Ratio 类可以实现与以下类型的相加：
	•	int
	•	float
	•	Ratio

还可以支持左操作数不是 Ratio 的情况（如 0.2 + Ratio(...)）

⸻

🔷 一、类型分派（Type Dispatching）

✅ 含义：

根据参数 other 的类型，采用不同的处理逻辑。

✅ 应用示例：

if isinstance(other, int):
    ...
elif isinstance(other, Ratio):
    ...
elif isinstance(other, float):
    ...

✅ 作用：

支持与不同类型的对象进行加法操作，避免报错或逻辑混乱。

⸻

🔷 二、类型强制转换（Type Coercion）

✅ 含义：

将当前对象转换成另一种类型，以便与该类型兼容操作。

✅ 应用示例：

elif isinstance(other, float):
    return float(self) + other

def __float__(self):
    return self.number / self.denom

✅ 作用：

支持 Ratio + float 或 float + Ratio，自动转换成 float 运算。

⸻

🔁 三、反向加法操作（__radd__）

✅ 含义：

当 Ratio 出现在右边（如 0.2 + Ratio(...)）时，Python 会尝试调用 Ratio.__radd__。

✅ 实现方式：

__radd__ = __add__

✅ 作用：

实现加法操作的左右对称性，提高类的灵活性。

⸻

🧠 总结对比表

策略	含义	例子	目的
类型分派	根据类型决定执行逻辑	if isinstance(other, int)	支持多种类型操作
类型强制转换	主动转换成另一种类型	float(self)	兼容 float 等内建类型
反向操作支持	支持 float + Ratio	__radd__ = __add__	保证操作顺序不影响正确性


⸻

📚 延伸阅读
	•	Python 官方文档：
	•	数据模型（含特殊方法）
	•	相关魔术方法：
	•	__add__()、__radd__()、__float__()、__str__()、__repr__()