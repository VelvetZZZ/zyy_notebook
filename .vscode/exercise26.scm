;Scheme Lists
(display (cons 1 (cons 2 '())))
(newline)

(define x (cons 1 (cons 2 '())))
(display(car x))
(newline)

(display(cdr x))
(newline)

(display(cons 1 (cons 2 (cons 3 (cons 4 '())))))