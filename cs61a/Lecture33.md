# Programs as Data 程序就是数据

## A Scheme Expression is a Scheme List

> 在 Scheme 中：程序 = 表达式，而表达式本质上就是列表（list）

### Scheme 程序由两类表达式组成

Scheme 程序中的表达式（expression）有两类：

#### 1）Primitive expressions（基本表达式）
例子
```scheme
2
3.3
true
+
quotient
```
基本表达式的特点：
	•	不是组合式，直接表示一个值或名称
	•	求值方式很简单：
	•	字面量 → 自己
	•	名字 → 在环境中找它的绑定

#### 2）Combinations（组合式）
也就是用 括号 + 列表结构 写成的函数调用（procedure call）或特殊形式（special form）：
```scheme
(quotient 10 2)
(not true)
(+ 2 3)
```
#### 这类表达式本质上都是：
一个 list，car 是 operator，cdr 是 operand 列表

一个表达式 ----> 一个列表结构

表达式结构：Operator 与 Operand

在 Scheme/Lisp 语言中，所有的函数调用或特殊形式都采用**前缀表示法**（Prefix Notation），并统一使用**列表结构**来表示：

* **基本结构：** `(操作符 操作数1 操作数2 ...)`

#### 术语定义：

| 术语 (英文) | 中文 | 含义 | 对应列表结构 |
| :--- | :--- | :--- | :--- |
| **Operator** | **操作符 / 过程** | 列表中第一个元素，表示要执行的**动作**或**函数**。 | `car` |
| **Operand** | **操作数 / 运算元** | 列表中剩余的元素，表示操作符作用的**数据**或**参数**。 | `cdr` 列表 |

**示例：** `(+ 2 3)`
* `Operator` 是 `+` (加法函数)。
* `Operands` 是 `2` 和 `3` (被加数)。