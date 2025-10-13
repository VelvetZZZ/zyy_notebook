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
