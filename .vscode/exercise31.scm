;Scheme Evaluation
(quote (1 2));is equivalent to
'(1 2)
;which evaluates to the list (1 2)
(quote hello)
'hello
(quote (1 2 3))
'(1 2 3)
(quote (+ 1 2))
'(+ 1 2)
(+ 1 2)        ; 注意：这个会执行