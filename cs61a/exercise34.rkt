#lang racket
;; 1. 引入兼容包
(require compatibility/defmacro)

;; 2. 定义 print
(define (print x)
  (display x)
  (newline))

;; 3. 宏定义
(define-macro (twice expr)
  (list 'begin expr expr))

;; 4. 测试
(display "--- Test Start ---\n")
(twice (print 2))
(display "--- Test End ---\n")