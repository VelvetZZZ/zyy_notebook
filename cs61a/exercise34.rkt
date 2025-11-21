#lang racket
;; 1. 引入兼容包 (为了支持 define-macro)
(require compatibility/defmacro)

;; 2. 【关键】引入 Racket 自带的追踪库
(require racket/trace) 

(define (print x)
  (display x)
  (newline))

;; =========================================================
;; 练习 1：Twice Macro
;; =========================================================
(display "\n=== 练习 1: Twice Macro ===\n")
(define-macro (twice expr)
  (list 'begin expr expr))

(twice (print 2))

;; =========================================================
;; 练习 2：Tracing Fact (Racket 专用版)
;; =========================================================
(display "\n=== 练习 2: Tracing Fact ===\n")

;; 1. 定义正常的递归函数
(define (fact n)
  (if (zero? n) 1 (* n (fact (- n 1)))))

;; 2. 【核心魔法】开启追踪！
;; 这行代码会自动帮你完成 PPT 里那堆复杂的“劫持”工作
(trace fact)

;; 3. 测试
(fact 5)