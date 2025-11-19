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

### 组合式 = 列表

> Scheme 的列表数据结构（cons 链表）可以直接表示代码中的组合式。

#### 看看下面的表达式：

(list 'quotient 10 2)
求值后得到：
(quotient 10 2)
它不是执行 quotient，而只是把这个结构构造出来。

也就是说：

```text
list + quote = 构造“代码本身”
```
这就是 Scheme 的“代码即数据（code as data）”哲学。

### eval 可以执行这个表达式！

```scheme
(eval (list 'quotient 10 2))
```
#### 运行过程：
	1.	(list 'quotient 10 2) 生成列表结构 (quotient 10 2)
	2.	eval 读取这个列表，把它当作 Scheme 表达式执行
	3.	执行结果是：5

你会发现：

我们用 list 构造了一个程序，然后让 eval 执行了这个程序！

这让 Scheme 有了 **“元编程”** 的能力（program writes program）。

### 为什么这是解释器课程的关键？

因为下一步老师要教你写：

一个 Scheme 解释器（Meta-circular Evaluator）

要写解释器，你必须先理解：
	1.	Scheme 程序的结构是什么？（它是列表）
	2.	如何区分操作符与操作数？（car / cdr）
	3.	如何对表达式进行模式匹配？
	4.	“代码即数据（code as data）” 的思想

这是构建解释器的基础。

### 总结：
Scheme 表达式就是 Scheme 列表，因此 Scheme 语言可以用自己的数据结构来表示、操作、构造和执行代码。


## Scheme：quote 与 list

### 1. quote（'）是什么？

定义：quote 用来阻止求值，把后面的东西当作“数据”而不是“代码”。
其缩写形式是 '。

作用总结
	•	quote 返回“原样表达式”
	•	quote 让表达式变成数据
	•	quote 是 写解释器 和 元编程 的核心

“quote 保护代码，让它保持数据形态。”

### 2. list 是什么？

定义：list 用来构造一个 Scheme 列表（链表结构）。

#### 为什么重要？
因为在 Scheme 中：

一个组合式（函数调用）就是一个列表
比如：(quotient 10 2)
本质是：'(quotient 10 2)

你可以用 list 自己构造这个表达式：

(list 'quotient 10 2)
→ (quotient 10 2)

### 3. quote + list 的威力：代码即数据
示例：
(list '+ 1 2)
→ (+ 1 2)
现在它只是一个数据结构，还没执行。
你可以执行它：
(eval (list '+ 1 2))
→ 3
 **程序生成程序，再执行程序：元编程(Meta-programming)**

 