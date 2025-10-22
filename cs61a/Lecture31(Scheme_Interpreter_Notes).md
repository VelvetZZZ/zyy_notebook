# Scheme 学习笔记：解释器与作用域

## 1. Lambda Expressions in Scheme

### 基本语法
```scheme
(lambda (<formal-parameters>) <body>)
```
示例：
```scheme
(lambda (x) (* x x))
```
这是一个匿名函数，接受一个参数 `x`，返回 `x` 的平方。

### 解释器中的处理方式

解释器遇到 lambda 表达式时不会立即执行，而是将其转化为一个 **过程对象（procedure object）**，该对象包含：

- `formals`：形式参数列表
- `body`：函数体表达式
- `env`：定义时的环境（Frame）

### Python中模拟的类结构

```python
class LambdaProcedure:
    def __init__(self, formals, body, env):
        self.formals = formals  # Scheme参数列表（symbols）
        self.body = body        # Scheme表达式（过程体）
        self.env = env          # 定义该lambda时的环境
```
此类用于模拟 Scheme 中的 lambda 表达式在解释器中被“求值”后的表示。

> 注意：这个过程不是编译器做的，而是解释器在**运行时**自动完成的。

---

## 2. Frame与变量作用域（Environment Model）

### Frame 的概念

解释器中，Frame 表示一个环境作用域（scope），用于存储变量绑定。每个 Frame 可能有一个“父 Frame”，形成一个**作用域链（环境链）**。

```python
g = Frame(None)     # 创建全局Frame
f1 = Frame(g)       # f1是g的子Frame
```

### define 与 lookup 操作

```python
g.define('x', 3)
g.define('z', 5)
f1.define('x', 2)
f1.define('z', 4)
```

变量定义后，在 Frame 中查找变量时会按如下规则：

1. 先查找当前 Frame（局部作用域）
2. 再查找父 Frame（如全局作用域）
3. 一直向上直到找到或报错

```python
f1.lookup('x')  # 返回 2 （局部x）
f1.lookup('z')  # 返回 4 （局部z）
g.lookup('z')   # 返回 5 （全局z）
```

### 局部优先查找原则

老师强调：

> "We look in the local frame before we look in the global frame."

即：解释器总是优先查找“局部作用域”的绑定，如果找不到才会查找父 Frame。这是实现**词法作用域（Lexical Scoping）**的关键机制。

---

## 3. 总结

- Scheme中的lambda表达式会被转换为包含`formals`、`body`、`env`的过程对象（LambdaProcedure）
- `env` 保证了闭包的实现，可以保留定义时的环境上下文
- Frame 表示作用域环境，形成链式结构，用于变量查找
- `lookup` 总是局部优先，体现了词法作用域的规则

本知识点是 Scheme 解释器实现的基础，理解这一部分有助于你深入掌握函数式语言的本质与解释器的运行原理。
