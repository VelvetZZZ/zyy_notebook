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
