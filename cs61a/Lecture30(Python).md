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
