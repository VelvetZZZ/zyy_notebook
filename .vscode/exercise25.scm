(begin
  (display "Hello, Scheme!")
  (newline)

  (define pi 3.14)
  (display (* pi 2))  ; ✅ 显示计算结果
  (newline)
)



(define (plus4 x) (+ x 4))
;same as
(define plus4 (lambda (x) (+ x 4)))