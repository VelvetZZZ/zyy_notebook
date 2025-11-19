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