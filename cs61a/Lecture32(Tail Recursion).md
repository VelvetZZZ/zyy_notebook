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