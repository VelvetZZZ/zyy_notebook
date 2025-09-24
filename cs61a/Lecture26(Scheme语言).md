# 📘 Scheme Fundamentals 学习笔记

> 来源：伯克利 CS61A 《Structure and Interpretation of Computer Programs》

---

## 🧠 一、表达式（Expressions）

Scheme 程序是由一系列表达式组成的，表达式可以分为两类：

### 1. 🧩 原始表达式（Primitive Expressions）

最基本的值或运算符：

- 数字：`2`, `3.3`
- 布尔值：`true`, `false`
- 运算符：`+`, `-`, `quotient`, `not` ...

### 2. 🧱 组合表达式（Combinations）

用括号包住操作符和参数，表示函数调用：

- `(quotient 10 2)` → 返回 `5`
- `(not true)` → 返回 `false`

---

## 🔁 二、语义规则（Evaluation Rules）

### ✔️ 数字是自求值的（Self-evaluating）

```scheme
> 2
2
```
### ✔️ 符号是变量名（Symbols）

如 quotient 表示 Scheme 的整数除法函数。

## 🧩 三、函数调用表达式（Call Expressions）
格式如下：
```scheme
(<operator> <operand1> <operand2> ...)
```
•操作符：函数名，例如 +, *, quotient
•操作数：可以是数字、符号、嵌套的表达式

## 🧪 四、示例讲解（Examples）
- 示例 1： 
 (quotient 10 2) ; → 5

调用 quotient，将 10 整除以 2，结果为 5。

- 示例 2（嵌套调用）：
 (quotient (+ 8 7) 5) ; → 3 
1.	(+ 8 7) → 15
2.	quotient(15, 5) → 3

- 示例 3（多重嵌套）：
步骤分析：
1.	(+ 2 4) → 6
2.	(* 3 6) → 18
3.	(+ 3 5) → 8
4.	(- 10 7) → 3
5.	(+ 18 8 3 6) → 35 

## 📌 五、语法提示（Syntax Notes）
✅ 表达式使用 前缀记法（operator 写在前）
✅ 使用圆括号表示函数调用（不能省略）
✅ 表达式可以 跨行 书写，空格与换行 不影响求值
❌ 不要漏括号，括号必须匹配完整！

## 核心语法：前缀表示法(Prefix Notation)
- 在我们常见的语言 (如 Java, Python) 中，我们使用中缀表示法：3 < 5 (操作符在中间)。

- 在 Scheme 中，操作符永远在最前面，并用括号括起来：(< 3 5)。


# 🧠 Scheme Special Forms 学习笔记

## 🌟 什么是 Special Form（特殊形式）？

> 在 Scheme 中，**不是函数调用的表达式就是特殊形式**（special form）。

特殊形式不会一开始就对所有参数求值，而是根据语法规则选择性地求值。例如 `if` 只会求值其中一个分支。

---

## ✅ 常见的 Special Forms

### 1. `if` 表达式（条件判断）

```scheme
(if <predicate> <consequent> <alternative>)
```
(if <测试条件> <条件为真时的返回值> <条件为假时的返回值>)

语义解释：
•	先判断 <predicate> 条件是否为真
•	如果为真，返回 <consequent>
•   否则，返回 <alternative>
📌 只会执行其中一个分支！
例子：
(if (< 3 5) 1 2)   ; 返回 1
•解释：
<测试条件>: (< 3 5)
这本身也是一个表达式。
它的意思是 "判断 3 是否小于 5"。
这个判断的结果是 真 (True)。
<条件为真时的返回值>: 1
如果 <测试条件> 的结果是真，整个 if 表达式就返回这个值。
<条件为假时的返回值>: 2
如果 <测试条件> 的结果是假，整个 if 表达式就返回这个值。