# 🧠 Programming Languages 编程语言

## 一、概述（Overview）

> 一台计算机可以执行用多种编程语言编写的程序。

编程语言是人与计算机交流的媒介，它们存在于不同的 **抽象层级**。  
从底层到高层，大致可以分为两类：

---

## 🧩 二、Machine Languages（机器语言）

### 🌟 定义
- 机器语言是 **计算机硬件能直接理解的语言**。  
- 每个 CPU 都有自己的 **指令集（Instruction Set Architecture, ISA）**。

### 🧱 特点
- **由硬件直接解释执行**（不需要其他程序翻译）。  
- 每一条指令由固定的二进制编码组成，用于控制：
  - 算术运算（加、减、乘、除）
  - 内存读写（访问特定地址）
  - 控制流（跳转、条件判断）

### ⚙️ 缺点
- 与具体硬件结构 **强绑定**，不同 CPU 架构不兼容。
- 没有抽象机制：  
  ➜ 操作的是**具体的内存地址**和**寄存器**，  
  ➜ 代码难以阅读、难以维护。

---

## 🧠 三、High-Level Languages（高级语言）

### 🌟 定义
- 高级语言是由 **另一个程序（解释器或编译器）** 来执行或翻译的语言。  
  例如：Python、C、Java、Scheme。

### 💡 特点
- **提供抽象能力（abstraction）**：
  - 变量命名（naming）
  - 函数定义（function definition）
  - 类与对象（object-oriented abstraction）
- **屏蔽底层细节**：  
  程序可以独立于硬件与操作系统运行。

### 🎯 优势
- 让程序员专注于 **逻辑与结构**，而非硬件操作。
- 使得软件开发更快、更可靠。

---

## 🐍 四、Python 示例：从源码到字节码

### 示例代码
```python
def square(x):
    return x * x
```

### 分析：
1. 这是一段 **高级语言**（Python）代码。
2. Python 解释器不会直接让 CPU 执行，而是先编译成 **字节码（Byte Code）**。

### 生成字节码示例
```python
from dis import dis
dis(square)
```

输出（Python 3 Byte Code）：
```
LOAD_FAST     0 (x)
LOAD_FAST     0 (x)
BINARY_MULTIPLY
RETURN_VALUE
```

### 解释
- `LOAD_FAST 0 (x)`：加载变量 `x`
- `BINARY_MULTIPLY`：执行乘法
- `RETURN_VALUE`：返回结果  

➡️ **字节码**是 Python 的中间语言（Intermediate Representation），  
由 **解释器** 转换为底层机器指令执行。

---

## 🧩 五、总结对比

| 分类 | 执行方式 | 抽象层次 | 可移植性 | 示例 |
|------|------------|------------|------------|------|
| 机器语言 | 直接由硬件执行 | 最底层 | ❌（依赖CPU） | 二进制指令 |
| 高级语言 | 由解释器或编译器执行 | 高层 | ✅（跨平台） | Python、C、Java |

---

## 💬 六、课程核心思想

> “Everything we’ve learned in this course is about high-level languages that are used to build software today.”

即：  
> 本课程讲的一切，都是关于 **现代软件开发中使用的高级语言**。  
> 机器语言虽基础，但我们更关注抽象层面的编程逻辑与结构。

# 🧠 Metalinguistic Abstraction（元语言抽象）

## 一、核心思想

> 一种强大的抽象方式，是**定义一种新的语言**，使其专门适配某一类应用场景或问题领域。

也就是说：
> 当现有编程语言不够灵活或简洁时，我们可以**创造一门新的语言**，让它更容易描述特定类型的问题。

---

## 🧩 二、概念理解

“Metalinguistic Abstraction” 指的是：
> **使用一种语言来定义另一种语言** 的能力。

它是**抽象的最高层次**。  
举例：  
- 用 Python 来写一个“小语言”解释器；  
- 用 Lisp 来定义新的语法规则；  
- 用正则表达式定义匹配规则。  

这些都是 **“用语言定义语言”** 的例子。

---

## 💡 三、两种常见动机

### 1️⃣ Type of Application（应用类型导向）
> 根据特定“应用类别”设计语言。

- **示例：Erlang**  
  - 设计目标：支持**并发编程（concurrent programs）**  
  - 内建机制：用于表达并行通信（concurrent communication）  
  - 实际用途：用于实现支持大量并发连接的聊天服务器、通信系统等。

👉 语言的语法与运行时都专门为某类任务而优化。

---

### 2️⃣ Problem Domain（问题领域导向）
> 根据特定“问题领域”设计语言。

- **示例：MediaWiki Markup Language（维基标记语言）**  
  - 设计目标：生成**静态网页内容**。  
  - 内建功能：文本格式化（text formatting）、页面链接（cross-page linking）  
  - 应用场景：创建维基百科页面。

👉 语言结构与语义完全贴合“网页内容生成”的需求。

---

## 🧱 四、编程语言的基本组成

一门编程语言至少包含：

| 概念 | 含义 |
|------|------|
| **Syntax（语法）** | 语言中允许的合法语句与表达式形式（结构） |
| **Semantics（语义）** | 这些语句的执行/求值规则（意义） |

例如在 Python 中：
```python
x = 2 + 3   # Syntax: 合法语句
# Semantics: 执行时，计算 2+3 并将结果赋给 x
```

---

## ⚙️ 五、创建一门新的编程语言需要什么？

要设计或实现一门新的语言，通常需要以下两项之一：

| 要素 | 含义 |
|------|------|
| **Specification（规范说明）** | 语言的正式文档，定义其语法（syntax）和语义（semantics） |
| **Canonical Implementation（规范实现）** | 该语言的解释器或编译器（负责执行或翻译程序） |

---

### ✅ 举例说明：

- **Python**
  - **Specification**：Python Language Reference（定义语法与语义）  
  - **Canonical Implementation**：CPython（解释器）

- **HTML**
  - **Specification**：由 W3C 定义的 HTML 标准  
  - **Implementation**：各浏览器的渲染引擎（Chrome 的 Blink、Firefox 的 Gecko 等）

---

## 🧩 六、总结与课程联系

| 抽象层级 | 含义 |
|------|------|
| **普通抽象** | 用函数、对象封装重复逻辑 |
| **高阶抽象** | 用函数操作函数（如 `map`, `reduce`） |
| **元语言抽象（Metalinguistic）** | 用语言定义语言（如创建解释器、DSL） |

---

## 💬 教授核心观点

> “A powerful form of abstraction is to define a new language.”

也就是说：  
> 编程的最高层次，不是使用语言，而是**创造语言本身**。  
> 当你能定义新的语法与语义，你就能完全掌控表达方式。
