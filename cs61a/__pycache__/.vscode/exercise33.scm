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