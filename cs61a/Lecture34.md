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