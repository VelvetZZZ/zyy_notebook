# 📘 Python 异常处理 —— Raise Statements

## 🔹 基本语法

Python 中的异常通过 **`raise`** 语句抛出：

```python
raise <expression>
```

其中 `<expression>` 必须是：
- 一个 **`BaseException`** 的子类，或  
- 该子类的一个实例。

---

## 🔹 异常对象的构造

异常（Exception）与其他对象一样，可以被直接构造。例如：

```python
raise TypeError('Bad argument!')
```

这会创建并抛出一个 `TypeError` 异常对象。

---

## 🔹 常见的内置异常类型

Python 提供了许多 **内置异常（built-in exceptions）**，以下是一些常见示例：

| 异常类型 | 触发场景 |
|-----------|-----------|
| **`TypeError`** | 函数接收到错误类型或数量的参数 |
| **`NameError`** | 使用了未定义的变量名 |
| **`KeyError`** | 字典中查找不存在的键 |
| **`RecursionError`** | 递归调用过多导致栈溢出 |

---

## 💡 备注
> 以上这些错误类型都是 **Python 内置（built-in）** 的异常类，可直接使用，无需导入。


# 内置函数 isinstance

```python
isinstance(object, classinfo)
```
参数         含义
object     你想要检测的对象
classinfo  类型或类型元组（tuple）

✅ 返回值
•如果 object 是指定类型的实例（或子类实例），返回 True
•否则返回 False

# Python isinstance() 与 type() 的区别

## 一、示例代码

```python
class Animal: pass
class Dog(Animal): pass

d = Dog()
print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True ✅
print(type(d) == Animal)       # False ❌
```

---

## 二、逐行讲解

### 1️⃣ 定义类

```python
class Animal: pass
class Dog(Animal): pass
```
- `Animal` 是父类（基类）。  
- `Dog` 是子类，继承自 `Animal`。  
➡️ 意味着：**Dog 拥有 Animal 的所有特征**。

---

### 2️⃣ 创建实例

```python
d = Dog()
```
现在 `d` 是一个 `Dog` 类型的对象。

---

### 3️⃣ `isinstance(d, Dog)` ✅

```python
print(isinstance(d, Dog))  # True
```
判断 `d` 是否是 `Dog` 的实例。  
✅ 答案是 True，因为 `d` 就是通过 `Dog()` 创建的。

---

### 4️⃣ `isinstance(d, Animal)` ✅

```python
print(isinstance(d, Animal))  # True
```
判断 `d` 是否是 `Animal` 的实例。  
✅ 结果仍然是 True，因为 `Dog` 是 `Animal` 的子类。  
`isinstance()` 会**考虑继承关系**。

📘 举个比喻：  
> “狗是一种动物” → 所以 `Dog` 也是 `Animal`。

---

### 5️⃣ `type(d) == Animal` ❌

```python
print(type(d) == Animal)  # False
```
`type()` 返回对象的**确切类型**，不考虑继承。  
这里 `type(d)` 是 `Dog`，不是 `Animal`，所以结果为 False。

---

## 三、对比总结

| 函数 | 是否考虑继承 | 示例结果 |
|------|---------------|-----------|
| `isinstance(d, Dog)` | ✅ 是 | True |
| `isinstance(d, Animal)` | ✅ 是 | True |
| `type(d) == Animal` | ❌ 否 | False |

---

## ✅ 结论

- `isinstance()` 更灵活，更推荐在面向对象编程中使用；  
- `type()` 仅用于你需要**精确判断类型**时使用。

# 🐍 Python 异常处理 —— Try 语句 (Try Statements)

## 一、概念

> **Try statements handle exceptions**
>
> `try` 语句用于捕获并处理程序运行中发生的异常，使程序不会因为错误而崩溃。

---

## 二、基本语法结构

```python
try:
    <try suite>
except <exception class> as <name>:
    <except suite>
```

### 各部分解释

| 部分 | 含义 |
|------|------|
| `try:` | 开始一个可能出错的代码块 |
| `<try suite>` | 要执行的代码（可能抛出异常） |
| `except <exception class> as <name>:` | 捕获指定类型的异常，将异常对象命名为 `<name>` |
| `<except suite>` | 当捕获到异常时要执行的代码 |

---

## 三、执行规则 (Execution rule)

1️⃣ **执行顺序**  
- 先执行 `try` 块中的代码。  
- 如果没有发生异常 → 跳过 `except`，程序继续运行。

2️⃣ **如果发生异常**  
- 当 `try` 块中出现异常时：  
  - Python 会查找匹配的 `except` 分支；  
  - 如果异常类型匹配 → 执行对应的 `except` 代码；  
  - 若写了 `as <name>`，异常对象会绑定到 `<name>` 变量；  
  - 执行完 `except` 后，程序继续向下运行（不会崩溃）。

---

## 四、示例讲解

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
```

运行效果：

| 输入 | 输出 | 说明 |
|------|------|------|
| `5` | `2.0` | 正常执行 |
| `0` | `Cannot divide by zero: division by zero` | 捕获异常并继续运行 |

---

## 五、示例：打印错误但继续执行

> “If the except suite just says, you know, print out an error message but keep running, that’s exactly what will happen.”

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Oops, division by zero!")  # 打印错误信息
print("Program continues...")
```

输出结果：

```
Oops, division by zero!
Program continues...
```

✅ 程序没有崩溃，而是继续运行。

---

## 六、小结

| 概念 | 含义 |
|------|------|
| `try` | 包含可能出错的代码 |
| `except` | 定义异常的处理方式 |
| `as <name>` | 获取异常对象 |
| 程序流程 | try → except（如果异常） → 继续执行 |
| 优点 | 防止程序崩溃，提供友好的错误处理机制 |

---

💡 **结论：**
`try-except` 是 Python 异常处理的核心机制。  
合理使用它，可以让程序更加健壮、可控。

