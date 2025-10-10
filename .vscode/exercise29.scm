(define a 1)
(define b 2)
(display(list a b))
(newline)
(display "Result: ")
(display (list a b))
(newline)

(display(list 'a 'b))
(newline)
(display(list 'a b))
(newline);Quatation

;Quotation can also be applied to combinations to from lists.
(display'(a b c))
(newline)
(display(car '(a b c)))
(newline)

(display 'a)
(display (quote a))
(newline)
#|
(cons 'a nil)
nil 在 MIT Scheme 里不是定义好的变量，
而是 Common Lisp 的空表符号。
在 Scheme 里应该使用 '() 表示空表。
|#

(display (cons 'a '()))
(newline)
(display (cons (quote a) '()))
(newline)
#|单引号的好处是节省了一组嵌套的括号|#

'(1 2);(1 2)
'(1 a);(1 a)
(list 1 'a);(1 a)
(list 1 a);Error:unknown identifier:a
#|在定义a之前无法对其进行评估,
但可以在定义之前引用a,因为它只是一个符号|#

;List Processing
(display(append '(1 2) '(3 4)))
(newline)

(display(map (lambda (x) (* x x)) '(1 2 3 4)))
(newline)

(display(filter (lambda(x)(> x 2)) '(1 2 3 4 5)))
(newline)

(display(apply + '(1 2 3 4)))
(newline)




