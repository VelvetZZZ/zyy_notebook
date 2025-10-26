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


