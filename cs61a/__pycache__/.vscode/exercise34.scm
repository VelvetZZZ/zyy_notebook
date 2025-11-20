;Discussion Question: Pythagorean Theorem 勾股定理

(define (square-expr term) `(* ,term ,term))
`(+ ,(square-expr 'a) ,(square-expr 'b))


;Macros宏
;Macros Perform Code Transformations
(define-macro (twice expr)
   (list 'begin expr expr))
   (display(twice (print 2)))