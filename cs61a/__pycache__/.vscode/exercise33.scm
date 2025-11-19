(define (fact n)
(if (= n 0)
1
(* n (fact (- n 1)))))
(display (fact 5))
(newline)

(define (fact-exp n)
(if ( = n 0) 
1
(list '* n (fact-exp(- n 1))'))) 
(display (fact-exp 5))
(newline)

(define (fib n)
(if (<= n 1) n (+ (fib (- n 2))(fib (- n 1)))))
(display (fib 6))
(newline)

(define (fib-exp n)
    (if (<= n 1) n (list '+ (fib-exp (- n 2)) (fib-exp (- n 1)))))
    (display (fib-exp 6))
(newline)
    (display(eval (fib-exp 6)))
(newline)

;Generating Code
;Quasiquotation 准引用 `,
;逗号 , 用于取消引用
;逗号加 at ,@ 用于取消引用并展开列表
;Example:While Statements
(begin
(define (f x total)
   (if (< x 10)
    (f (+ x 2) ( + total (* x x))))
    total))
(f 2 0)
(newline)

(begin
(define(f x total)
(if (< (* x x) 50)
 (f (+ x 1) (+ total x))
 total))
(f 1 0))
(display (f 1 0))
(newline)



(define (sum-while initial-x condition add-to-total update-x)
  `(begin
     (define (f x total)
       (if ,condition
           (f ,update-x (+ total ,add-to-total))
           total))
     (f ,initial-x 0)))
(display (eval (sum-while 1 '(< (* x x) 50) 'x '(+ x 1))))
(newline)


