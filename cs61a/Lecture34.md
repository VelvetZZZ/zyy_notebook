# 学习笔记：Scheme 元编程与代码生成 (勾股定理案例)

## I. 核心目标
利用 Scheme 的**准引用 (Quasiquotation)** 机制，编写代码来**生成**勾股定理的数学表达式 `(+ (* a a) (* b b))`，而不是直接计算它的值。


## II. 解决方案代码

### 1. 定义“平方表达式”生成器
我们要定义一个函数，输入一个符号（如 `'a`），输出一段代码列表（如 `(* a a)`）。

```scheme
;; 填空：
;; 1. 使用 ` (反引号) 创建列表模板
;; 2. 使用 , (逗号) 插入 term 的值
(define (square-expr term)
  `(* ,term ,term))
```

### 2. 拼接完整的勾股定理公式
我们要构建最外层的加法结构，并将上面生成的子表达式插入进去。

1. 使用 ` (反引号) 创建加法模板 (+ ... ...)
2. 使用 , (逗号) 执行函数调用，并插入生成的列表
`(+ ,(square-expr 'a) ,(square-expr 'b))

最终输出结果 (一段代码/列表)：
(+ (* a a) (* b b))

## III. 核心逻辑解析 (冷冻机与微波炉)

这个案例完美展示了“代码即数据”的思维切换：

| 符号           | 名称             | 绰号        | 作用  | 在本例中的应用 |
| :---           |:---            | :---       | :---   | :---         |
| **`** | **Quasiquote (准引用)** | **冷冻机** ❄️ | **“抄写模式”**：把后面的内容当成数据列表冻结起来，不执行。 | 用于制造 `(* ...)` 和 `(+ ...)` 的**外壳结构**。 |



## IV. 常见陷阱：符号 (Symbol) vs 变量 (Variable)
在使用这个函数时，传入参数必须小心：

### 正确写法：

```scheme
(square-expr 'a)
```
- 原理： 'a 是一个 Symbol (符号)。
- 过程： 函数接收到符号 'a，把它放入列表。
- 结果： (* a a)

### ❌ 错误写法 (报错：unknown identifier)
```scheme
(square-expr a)
```
- 原理： a 没有引号，Scheme 认为它是 Variable (变量)。
- 过程： Scheme 试图去内存里找“变量 a 的值是多少？”
- 结果： 找不到定义，报错 Error: unknown identifier: a。

## V. 总结
元编程的本质：编写 “写代码的代码”。

square-expr 就像一个零件工厂，生产 (* a a) 这种零件。

最外层的调用就像装配线，把零件拼装成 (+ (* a a) (* b b)) 这种成品。

牢记口诀： 看到反引号 是在造壳子，看到逗号,` 是在填肉（求值）。


# Macros Perform Code Transformations (宏执行代码转换)
## I. 宏 (Macro) 的核心定义

定义：宏是一种在程序求值（Evaluation）之前，对源代码进行的操作。

"A macro is an operation performed on the source code of a program before evaluation."

适用性：宏存在于许多编程语言中，但在像 Lisp (Scheme) 这样的语言中定义起来最容易且正确。

## II. Scheme 中的实现
Scheme 使用 define-macro 这一特殊形式（Special Form）来定义源代码的转换规则。

### 1. 示例代码：twice 宏
这个宏的作用是将输入的表达式执行两次。

```Scheme

;; 定义宏
(define-macro (twice expr)
  (list 'begin expr expr))

;; 调用演示
;; 输入源代码： (twice (print 2))
;; 宏展开结果： (begin (print 2) (print 2))
;; 最终执行结果：
;; 2
;; 2
```
### 2. 核心区别 (The Golden Rule)
这是宏与普通函数最本质的区别：

"Macros take in expressions and return expressions instead of taking in values and returning values." (宏接受表达式并返回表达式，而不是接受值并返回值。)

## III. 宏调用表达式的求值流程 (Evaluation Procedure)

当解释器执行一个宏调用时，遵循以下三个严格步骤：

- 评估操作符 (Evaluate the operator)

- 确认该操作符绑定的是一个宏（Macro）。

- 调用宏过程 (Call the macro procedure)

将操作数表达式（Operand expressions）作为参数传递给宏。

⚠️ 关键点：WITHOUT evaluating them first (不对参数进行求值，直接传代码文本)。

评估返回的表达式 (Evaluate the returned expression)

对宏过程返回的那段新代码（Expression）进行求值，这才是最终的执行步骤。



## Scheme 宏定义与语法扩展 (For 循环案例)

### I. 核心目标

利用 Scheme 的 宏 (Macro) 机制，为语言添加类似于 Python 的 for 循环 语法。 

我们需要编写宏代码，将用户输入的  for结构  转换 (Transform) 为 Scheme 底层支持的 map 调用，从而实现对列表的遍历求值。

### II. 解决方案代码

#### 1. 核心转换逻辑
宏的任务是充当“翻译官”。我们需要将左边的“源代码”翻译成右边的“可执行代码”。

- 源代码 (Source): (for x vals expr)

- 目标代码 (Target): (map (lambda (x) expr) vals)

#### 2. 定义 "for" 宏

我们要构造一个列表，其结构必须是 (map (lambda (sym) expr) vals)。 在这里，我们使用 list 函数来手动拼凑出这个列表结构。

```Scheme

;; 填空思路：
;; 1. 第一个元素是符号 'map
;; 2. 第二个元素是构造出的 lambda 表达式列表
;; 3. 第三个元素是直接传入的数据 vals
(define-macro (for sym vals expr)
  (list 'map
        (list 'lambda (list sym) expr)
        vals))
```

#### 3. 实际调用效果
当我们在解释器中运行这个宏时，它会先展开代码，再执行。

```Scheme

;; 调用：
(for x '(2 3 4 5) (* x x))

;; 宏展开后的等效代码 (系统自动执行)：
;; (map (lambda (x) (* x x)) '(2 3 4 5))

;; 最终输出结果：
;; (4 9 16 25)
```
#### 4.构造过程详解

我们需要拼凑出 (map (lambda (x) (* x x)) '(2 3 4 5)) 这个列表：

```scheme
'map:
```
列表的第一个元素是符号 map。

```scheme
(list 'lambda (list sym) expr):
```
列表的第二个元素是一个 lambda 表达式（也是一个列表）。

这里需要把传入的变量名 sym (即 x) 包在括号里 (list sym) 作为参数列表。

把 expr (即 (* x x)) 直接作为函数体。

```scheme
vals:
```
列表的第三个元素是直接传入的数据列表 '(2 3 4 5)。

### IV. 运行流程示例

当你运行 (for x '(2 3 4 5) (* x x)) 时：
- 传递参数:
  sym绑定为符号 'x
  vals绑定为列表 '(2 3 4 5)
  expr绑定为列表 '(* x x)
- 宏展开 (Expansion):
  Macro 内部执行 list 操作，生成新代码：

  (map (lambda (x) (* x x)) '(2 3 4 5))

- 求值 (Evaluation):

解释器执行这个生成的 map 表达式，计算出结果 (4 9 16 25)。