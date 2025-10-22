# Scheme & 编程语言作用域学习笔记：Lexical Scope 与 Dynamic Scope

---

## 🌟 什么是作用域（Scope）？

作用域是指：**程序在执行过程中如何查找变量绑定（变量的值）的位置**。

---

## 📘 1. Lexical Scope（词法作用域）

### ✅ 定义：
变量在函数 **定义时** 所在的环境中查找。这种作用域规则又称为 *static scope*。

### 🧠 查找路径：
1. 当前函数体中
2. 函数定义时的环境
3. 一直向上直到全局环境

### 💡 特点：
- 代码结构决定变量查找路径
- 行为可预测、易调试
- 现代语言（Scheme、Python、JavaScript、Java）普遍使用

### ✅ 示例：

```scheme
(define x 5)
(define (foo) x)
(define (bar) (let ((x 10)) (foo)))
(bar) ; => 5
```

即使 `foo` 在 `bar` 中被调用，但它定义时看到的 `x` 是全局的 `5`。

---

## 📕 2. Dynamic Scope（动态作用域）

### ✅ 定义：
变量在函数 **调用时** 所在的环境中查找。

### 🧠 查找路径：
1. 函数调用者的环境（即调用时的上下文）
2. 再往上查调用栈中的上一层环境

### 💡 特点：
- 调用位置决定查找路径
- 行为不易预测，调试困难
- 少数语言使用（早期 Lisp、Emacs Lisp、bash）

### ✅ 示例：

```scheme
(define f (lambda (x) (+ x y)))
(define g (lambda (x y) (f (+ x x))))
(g 3 7) ; => 13 （在 dynamic scope 下）
```

在 `f` 中使用了 `y`，虽然定义时看不到 `y`，但调用时 `g` 有 `y=7`，所以成功执行。

---

## 🧪 两种作用域结果对比：

代码：

```scheme
(define f (lambda (x) (+ x y)))
(define g (lambda (x y) (f (+ x x))))
(g 3 7)
```

| Scope 类型       | 查找规则               | 执行结果        |
|------------------|------------------------|------------------|
| Lexical Scope    | f 的 parent 是定义环境 | ❌ 报错：找不到 y |
| Dynamic Scope    | f 的 parent 是调用环境 g 的 Frame | ✅ 输出 13 |

---

## ⚙️ 是否可以两种作用域并存？

- ✅ 理论上可以（可以在解释器中实现）
- ⚠️ 实际上很少这样做，容易引发混乱
- Emacs Lisp 支持 dynamic scope，但可通过设置使用 lexical scope

---

## 🧱 用 Python 实现作用域模拟

你可以自己用 Python 实现作用域规则：

```python
class Frame:
    def __init__(self, parent):
        self.bindings = {}
        self.parent = parent

    def define(self, name, val):
        self.bindings[name] = val

    def lookup(self, name):
        if name in self.bindings:
            return self.bindings[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            raise NameError("Unbound variable: " + name)
```

想要动态作用域？调用函数时将 `caller_env` 设为 parent 即可！

---

## 🧠 总结：Lexical vs Dynamic Scope

| 项目 | Lexical Scope | Dynamic Scope |
|------|----------------|----------------|
| 查变量起点 | 函数定义时的环境 | 函数调用时的环境 |
| 易读性 | ✅ 好 | ❌ 差 |
| 可维护性 | ✅ 高 | ❌ 低 |
| 应用语言 | Python、Scheme、JS | Bash、Emacs Lisp（默认） |
| 示例结果 | 报错或正常，固定行为 | 行为依赖上下文调用 |

---

## 🎓 结语

理解作用域是掌握编程语言和解释器设计的核心。你可以用 Python/Scheme 完全“人工”实现作用域系统，甚至自由切换词法和动态作用域！
