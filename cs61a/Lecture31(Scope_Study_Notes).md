# Scheme 学习笔记：作用域与解释器结构

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

---

## 🧪 作用域行为对比：

| Scope 类型       | 查找规则               | 执行结果        |
|------------------|------------------------|------------------|
| Lexical Scope    | f 的 parent 是定义环境 | ❌ 报错：找不到 y |
| Dynamic Scope    | f 的 parent 是调用环境 g 的 Frame | ✅ 输出 13 |

---

## ⚙️ 两种作用域可以共存吗？

- ✅ 理论上可以（写解释器时控制 Frame parent）
- ⚠️ 实际上不推荐共存，容易产生困惑与 bug
- Emacs Lisp 提供切换 dynamic/lexical 的机制

---

## 🧱 Python 实现作用域查找（人工模拟）

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

---

## 🧠 解释器结构：Eval 与 Apply

### 🧩 Eval（evaluate）
- **理解表达式，判断要做什么**
- Base Cases：
  - 数字 → 直接返回
  - 变量 → 查找其绑定值（symbol lookup）
- Recursive Cases：
  - 函数调用 → eval 操作符 & 参数 → 再 apply
  - 特殊形式 → eval 各个子表达式

### 🧩 Apply（application）
- **执行过程或函数，做事情**
- Base Case：
  - 内建函数（如 `+`、`*`） → 直接调用
- Recursive Case：
  - 用户自定义函数 → 创建新环境 → eval 函数体

### 🔄 工作流程总结：

```scheme
(define square (lambda (x) (* x x)))
(square 5)
```

步骤：

1. `eval` 识别 `(square 5)` 是函数调用
2. `eval(square)` → 是个函数对象
3. `eval(5)` → 得到 5
4. `apply(square, 5)` → 创建新 frame，x=5
5. `eval(* x x)` → 最终计算出 25

---

## ✅ 总结：Eval vs Apply

| 函数 | 作用 | 比喻 |
|------|------|------|
| `eval` | 判断做什么 | “理解任务” |
| `apply` | 执行过程 | “完成任务” |

解释器本质上是通过这两个函数交替进行递归调用来解释一整门语言。理解这张结构图，你就理解了 Scheme 的解释器核心。

---
