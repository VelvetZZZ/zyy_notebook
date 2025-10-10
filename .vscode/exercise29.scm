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

(define s (cons 1 (cons 2 ())))
(display(map even? s))
(newline)
(display(filter even? s))
(newline)

(display(apply quotient '(10 5)))

;Example: Even Subsets  偶数子集
; ==========================================================
; even-subsets.scm
; Generate all non-empty subsets of integer list s
; that have an even or odd sum.
; ==========================================================

(define (even-subsets s)
  (if (null? s)
      '()  ; base case: empty list → no subsets
      (append
        (if (even? (car s))
            (map (lambda (t) (cons (car s) t))
                 (even-subsets (cdr s)))   ; 保持偶数性
            (map (lambda (t) (cons (car s) t))
                 (odd-subsets (cdr s))))   ; 翻转奇偶性
        (if (even? (car s))
            (even-subsets (cdr s))
            (odd-subsets (cdr s)))
        (if (even? (car s))
            (if (even? (car s)) (list (list (car s))) '())
            (if (even? (car s)) '() (list (list (car s))))))))

(define (odd-subsets s)
  (if (null? s)
      '()
      (append
        (if (odd? (car s))
            (map (lambda (t) (cons (car s) t))
                 (even-subsets (cdr s)))   ; 翻转奇偶性
            (map (lambda (t) (cons (car s) t))
                 (odd-subsets (cdr s))))   ; 保持奇数性
        (if (odd? (car s))
            (even-subsets (cdr s))
            (odd-subsets (cdr s)))
        (if (odd? (car s))
            (list (list (car s)))
            '()))))

; 测试
(display (even-subsets '(3 4 5 7))) (newline)
(display (odd-subsets '(3 4 5 7)))  (newline)



; ==========================================================
; even-odd-subsets.scm
; Non-empty subsets of integer list s that have even/odd sum
  改进版
; ==========================================================

(define (even-subsets s)
  (if (null? s)
      nil
      (append (even-subsets (cdr s))
              (subset-helper even? s))))

(define (odd-subsets s)
  (if (null? s)
      nil
      (append (odd-subsets (cdr s))
              (subset-helper odd? s))))

(define (subset-helper f s)
  (append
    (map (lambda (t) (cons (car s) t))
         (if (f (car s))
             (even-subsets (cdr s))
             (odd-subsets (cdr s))))
    (if (f (car s))
        (list (list (car s)))
        nil)))

; ======= Test ========
(display (even-subsets '(3 4 5 7 8))) (newline)
(display (odd-subsets '(3 4 5 7 8)))  (newline)




