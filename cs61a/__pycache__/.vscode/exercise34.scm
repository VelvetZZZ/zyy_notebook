;Discussion Question: Pythagorean Theorem 勾股定理

(define (square-expr term) `(* ,term ,term))
`(+ ,(square-expr 'a) ,(square-expr 'b))
