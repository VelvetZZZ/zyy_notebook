(define (square x) (* x x))
(define (cube x) (* x x x))

(display (+ (square 2) (cube 3)))
(newline)

(define (factorial n k)
    (if (zero? n) k
        (factorial (- n 1)
                   (* n k))))
(display (factorial 5 1))
(newline)
  
#| python equivalent
def factorial(n, k):
    while n > 0:
        n, k = n-1, k*n
    return k
print(factorial(5, 1))
|#


#Example:Length of a list
(define (length s)
    (if (null? s)
    0
    (+ 1 (length (cdr s)))))
#|不是尾递归|#

(define (length-tail s)
    (define(length-iter s n)
        (if (null? s) n
            (length-iter (cdr s) (+ n 1)))
            length-iter s 0))
(display (length-tail '(a b c d e f g h i j k l m n o p q r s t u v w x y z)))
(newline)
#|尾递归|#




