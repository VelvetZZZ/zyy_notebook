(begin
  (display "Hello, Scheme!")
  (newline)
)

(begin
  (define pi 3.14)
  (display (* pi 2))          ; ✅ 显示计算结果
  (newline)

  ;; 定义 square 函数
  (define (square x) (* x x))

  ;; 两种等价函数定义方式
  (define (plus4 x) (+ x 4))
  ; same as
  (define plus4 (lambda (x) (+ x 4)))

  ;; 匿名函数立即调用
  (display((lambda (x y z) (+ x y (square z))) 1 2 3))
  (newline)
)

(begin
(define x 11)
(cond((> x 10)(begin (print 'big) (print'guy)))
      (else   (begin(print 'small) (print 'fry))))
)