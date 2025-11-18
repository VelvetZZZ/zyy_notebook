# 🧠 Scheme 学习笔记：Tail Calls（尾调用）

## 📌 什么是 Tail Call（尾调用）？

- **尾调用**是指：一个过程调用在返回结果前没有其他操作要执行。也就是：某个函数调用发生在一个函数的最后一步，并且它的返回值被直接返回，而不需要再进行额外的计算。
- 换句话说，**“递归调用是这个函数的最后一步”**，那么这个调用就是尾调用。
- 在 Scheme 语言中，解释器应当支持“**无限数量的尾调用激活**”而只占用**常量空间**（constant space）！

---

## ✅ 为什么尾调用重要？

尾调用意味着：  
- 不需要为每一次调用分配新的栈空间。
- 程序更**节省内存**、更**高效**。
- 可以像迭代一样运行递归函数（因为空间不会不断增长）。

---

## 🎯 Tail Context（尾调用上下文）

尾调用必须出现在**tail context**中才有效。  
以下是**尾调用上下文**的常见位置：

1. **lambda 表达式中最后一个子表达式**  
   - 只有最后一个语句才是尾调用。

e.g.

(lambda (x)
  (display x)          ; 不是尾调用
  (+ x 1))             ; ✅ 是尾调用（最后一个表达式）

 (define (f x)
  (g x))               ; ✅ 是尾调用

2. **if 表达式中第2和第3个子表达式**  
   - `if <test> <then> <else>` 中的 `<then>` 和 `<else>` 可以是 tail context。

e.g.
(define (f x)
  (if (= x 0)
      0                          ; ✅ 是尾调用
      (g x)))                    ; ✅ 是尾调用

3. **cond 中所有非谓词（predicate）子表达式**  
   - 只要不是条件判断部分，就可以是尾调用上下文。
   - cond 就像是多重 if，每个匹配条件的分支中最后执行的表达式构成尾调用。

e.g.
(define (f x)
  (cond
    [(= x 0) 0]                  ; ✅ 是尾调用
    [(= x 1) (g x)]              ; ✅ 是尾调用
    [else (h x)]))               ; ✅ 是尾调用


### 📌 cond vs if 快速回忆

- **`if`：二选一**
  - 语法固定：`(if test then-expr else-expr)`
  - 只能处理**一个条件**与**两个结果**
  - 适合简单判断

- **`cond`：多分支选择器**
  - 写法：  
    ```scheme
    (cond
      [test1 expr1]
      [test2 expr2]
      [else expr-default])
    ```
  - 支持**多个条件依序判断**
  - 可读性强，替代层层嵌套的多个 if

- **本质关系**
  - `cond` 是多个 `if` 的语法糖  
    ```
    (cond [...] [...] [else e])  ≈  (if ... (if ... (if ... e)))
    ```

- **使用建议**
  - 简单条件 → `if`  
  - 多路判断 → `cond`  
  - 每个分支如果直接返回值，即为**尾调用位置**


4. **and / or 表达式中的最后一个子表达式**
- and 和 or 是逻辑表达式，只有最后一个子表达式是尾调用。

e.g.
(define (f x)
  (and (positive? x)
       (g x)))                   ; ✅ 是尾调用

5. **begin 表达式中最后一个子表达式**
- begin 表示顺序执行一组表达式，只有最后一行是尾调用。

e.g.
(begin
  (display "hello")
  (compute-result))             ; ✅ 是尾调用


## 💡 示例代码解释

```scheme
(define (factorial n k)
  (if (= n 0) 
      k
      (factorial (- n 1) (* k n))))
```
这段代码中的 (factorial (- n 1) (* k n)) 是一个 尾调用，因为它：
1.出现在 if 表达式的“else”部分（即 tail context）；
2.是函数中最后执行的操作，没有其他计算留在后面。
这就意味着这段递归代码空间开销不会随着递归层数增长，非常适合长递归！


## 🗣️ 英文解释摘要（PPT原文）

A procedure call that has not yet returned is active.
Some procedure calls are tail calls.
A Scheme interpreter should support an unbounded number of active tail calls using only a constant amount of space.



# 以列表长度计算为例：递归 vs 尾递归
(Eval with Tail Call Optimization
支持尾调用优化的Eval（求值过程）)

## 列表长度的普通递归版本

```scheme
(define (length s)
  (if (null? s)
      0
      (+ 1 (length (cdr s)))))
```
### 代码含义:
	•	(null? s)：判断列表是否为空
	•	空列表长度为 0
	•	非空列表长度 = 1 + 剩余列表长度
	•	(cdr s)：列表去掉第一个元素后的部分

*递归调用返回后，还要执行 + 1* 
因此递归调用不是整个函数的最终值，不属于尾调用。

### 结果:
	•	每层递归都需要等待下一层返回后进行加法
	•	调用栈会随着列表长度线性增长
	•	列表太长可能导致 **栈溢出**

##列表长度的尾递归版本

```scheme
(define (length-tail s)
  (define (length-iter s n)
    (if (null? s)
      n
      (length-iter (cdr s)(+ n 1))))
      (length-iter s 0))
```
### 代码含义:

该版本引入一个内部迭代函数：
	•	s：当前剩余列表
	•	n：累计计数器（已数到的长度）

### 流程：
	1.	初始调用 (length-iter s 0)，从 0 计数
	2.	每次递归都将：
	•	列表缩短（cdr s）
	•	计数器增加（(+ n 1)）
	3.	当 s 为空时返回 n
递归调用是整个 if 表达式的最终返回值：(length-iter (cdr s) (+ n 1))

### 优点
	•	Scheme 会对尾调用进行优化（TCO）
	•	不增长调用栈，空间复杂度为 O(1)
	•	相当于编译器把递归实现为循环

  尾递归相当于一个循环：
  while s not empty:
    s = cdr(s)
    n++
return n


## 🌀 Which Procedures Are Tail Recursive?（尾递归判断速记）

> **问题：下面哪些过程能在 Θ(1) 常量空间内运行？**  
> 判断标准：递归调用是否处于 **tail context（尾上下文）**。

---

###  什么是 Tail Context？

- **尾上下文（tail context）**：  
  一个函数调用作为“整个表达式的最终返回值”。  
  - 递归调用后 **不再有额外操作**
  - 解释器可进行 **尾调用优化（TCO）**
  - 栈帧不增长 → **空间 Θ(1)**

- **非尾上下文（not tail context）**：  
  调用结果还要参与其它计算（如 `+`, `*`, 比较等）。  
  - 栈帧持续增长 → **空间 Θ(n)**

---

## 1️⃣ `length` —— ❌ 非尾递归 → 空间 Θ(n)

```scheme
(define (length s)
  (+ 1
     (if (null? s)
         -1
         (length (cdr s)))))
```
红框部分：
	•	(length (cdr s)) 被包在 (+ 1 …) 内
	•	递归结果返回后 还有 pending work
	•	➤ 不在 tail context
	•	➤ 空间 Θ(n)

  ## 2️⃣ fib —— ❌ 非尾递归 → 空间 Θ(n)
```scheme
(define (fib n)
  (define (fib-iter current k)
    (if (= k n)
        current
        (fib-iter (+ current (fib (- k 1)))
                  (+ k 1)))))
```
	•	红框部分：
	•	fib 的递归结果要参与 (+ current …)
	•	不是尾调用
	•	➤ 不在 tail context
	•	➤ 空间 Θ(n)

## 3️⃣ contains —— ✔ 尾递归 → 空间 Θ(1)
```scheme
(define (contains s v)
  (if (null? s)
      false
      (if (= v (car s))
          true
          (contains (cdr s) v))))
```
	•	虚线框：
	•	(contains (cdr s) v) 是整个分支的返回值
	•	无额外操作
	•	➤ 在 tail context
	•	➤ 空间 Θ(1)
	•	💬 老师强调：
“contains already runs in constant space because it is tail recursive.”

## 4️⃣ has-repeat —— ✔ 空间 Θ(1)
```scheme
(define (has-repeat s)
  (if (null? s)
      false
      (if (contains? (cdr s) (car s))
          true
          (has-repeat (cdr s)))))
```

	注意两件事：

🔸 (1) contains? 调用 不在 tail context
	•	作为 if 的判断式
	•	不是最终返回值
	•	💬 老师：
“when it calls contains, that’s not a tail context.”

🔸 (2) 但整体空间仍是 Θ(1)
因为：
	•	has-repeat 对自身的调用在 tail context
	•	contains? 本身是尾递归 → 空间 O(1)
	•	两者均不积累栈帧

因此：
	•	➤ 整体空间仍是 Θ(1)
	•	💬 老师：
“the whole thing runs in constant space.”

> 只要所有递归不会生成未完成的操作（no pending work），解释器就可做 TCO → 空间 Θ(1)。
