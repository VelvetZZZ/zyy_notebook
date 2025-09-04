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