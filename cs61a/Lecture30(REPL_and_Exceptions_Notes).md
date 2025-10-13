# 🧮 Read–Eval–Print Loop (REPL) & Raising Exceptions 笔记

这两页讲的是解释器的“顶层运行机制”和“异常处理机制”。
也就是说：
- 前面的 `calc_eval`、`calc_apply` 定义了“解释器如何计算”  
- 而这里讲的 **REPL** 定义了解释器“如何和用户交互、循环运行”  
- **Raising Exceptions** 则解释了解释器在出错时如何处理错误。

---

## 🌀 一、Read–Eval–Print Loop（简称 REPL）

> The user interface for many programming languages is an **interactive interpreter**.

几乎所有解释型语言（包括 Python、Scheme、JavaScript 等）都有一个 REPL。  
它是解释器最外层的循环逻辑，让程序能够“读输入、求值、输出、再来一次”。

---

### 💡 REPL 的循环流程

1️⃣ **Print a prompt**
   - 输出提示符（如 `>>>`），提示用户输入代码。

2️⃣ **Read**
   - 读取用户输入的文本（如 `(+ 1 2 3)`）。

3️⃣ **Parse**
   - 解析文本输入为表达式结构（tokens → expression tree）。

4️⃣ **Eval**
   - 调用 `calc_eval` 对表达式求值。

5️⃣ **Print**
   - 输出结果值。

6️⃣ **Repeat**
   - 回到第 1 步，等待用户下一次输入。

---

### 🧠 流程图

```
┌──────────────┐
│  Print ">"   │
└──────┬───────┘
       ▼
┌──────────────┐
│  Read input  │
└──────┬───────┘
       ▼
┌──────────────┐
│  Parse text  │
└──────┬───────┘
       ▼
┌──────────────┐
│  Eval expr   │
└──────┬───────┘
       ▼
┌──────────────┐
│  Print val   │
└──────┬───────┘
       ▼
   (repeat)
```

---

### 🪄 关键思想

> **Read → Eval → Print → Loop**
> 
> 这是解释器与用户交互的最基本模式。  
> Python、Scheme、Lisp、Julia 等语言的交互式 Shell 都是基于 REPL。

---

## ⚠️ 二、Raising Exceptions（异常处理）

解释器在分析或求值时可能会遇到各种错误。  
这些错误通过抛出（raise）异常的方式报告。

---

### 📍 异常产生的阶段

| 阶段 | 可能抛出的异常 | 示例 | 异常说明 |
|------|----------------|------|-----------|
| **Lexical analysis** | `ValueError` | token `2.3.4` | 无效数字 → `invalid numeral` |
| **Syntactic analysis** | `SyntaxError` | 额外的 `)` | 语法错误 → `unexpected token` |
| **Eval** | `TypeError` | `()` | 空表达式不是数字或调用 → `() is not a number or call expression` |
| **Apply** | `TypeError` | `(-)` | 没有参数的运算 → `- requires at least 1 argument` |

---

### 🧩 核心思想

- 异常是程序在“解释过程中发现错误”时的信号。
- 解释器应当：  
  1. 捕获异常；  
  2. 打印错误信息（而不是崩溃）；  
  3. 继续 REPL 循环，让用户可以继续输入。

---

### 📘 举例说明

```python
# lexical analysis 阶段
# token 不合法
ValueError("invalid numeral")

# syntactic analysis 阶段
# 例如多一个 ')'
SyntaxError("unexpected token")

# eval 阶段
# 空的表达式
TypeError("() is not a number or call expression")

# apply 阶段
# 操作符没有参数
TypeError("- requires at least 1 argument")
```

---

## 🧠 三、REPL 与 Exception 的结合

在解释器的 REPL 中，我们通常这样组织代码：

```python
while True:
    try:
        src = input('calc> ')
        if src in ('exit', 'quit'):
            break
        expr = parse(src)
        val = calc_eval(expr)
        print(val)
    except Exception as e:
        print('Error:', e)
```

- 如果用户输入有问题，程序不会崩溃；
- 会打印错误提示（例如 `Error: unexpected token`）并继续循环；
- 这让解释器更健壮、可交互。

---

## ✅ 四、总结

| 模块 | 职责 |
|------|------|
| **REPL** | 定义解释器的交互循环：读取输入 → 解析 → 求值 → 输出 |
| **Exceptions** | 定义解释器在出错时的响应方式（抛出/捕获/报告错误） |

---

### ✳️ 一句话总结

> **REPL 是解释器的外层循环，让语言“活起来”；**  
> **异常机制是语言的防护网，让解释器“不会崩”。**

---
