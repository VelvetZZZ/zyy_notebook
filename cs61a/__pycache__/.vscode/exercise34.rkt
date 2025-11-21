#lang racket
(require compatibility/defmacro)

(define (print x)
  (display x)
  (newline))

;; --- 下面放你的宏定义 ---
(define-macro (twice expr)
  (list 'begin expr expr))

;; --- 下面是测试 ---
(display "--- Test Start ---\n")
(twice (print 2))


#lang racket
(require compatibility/defmacro)

;; 1. 定义宏：把 for 变成 map
(define-macro (for sym vals expr)
  (list 'map 
        (list 'lambda (list sym) expr) 
        vals))

;; 2. 测试运行
(display "Python style for-loop in Scheme:\n")

;; 这行代码在运行前，会被宏自动转换成 map
(display (for x '(2 3 4 5) (* x x)))