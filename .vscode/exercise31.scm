(begin
  (define (show label value)
    (display label)
    (display " => ")
    (write value)
    (newline))

  (show "1. 测试 quote 和原始表达式：(quote (1 2))" (quote (1 2)))
  (show "1. 同上：'(1 2)" '(1 2))

  (show "2. 测试 quote 和原始 symbol：(quote hello)" (quote hello))
  (show "2. 同上：'hello" 'hello)

  (show "3. quote 不会执行表达式：(quote (+ 1 2))" (quote (+ 1 2)))
  (show "3. 同上：'(+ 1 2)" '(+ 1 2))

  (show "4. 这个会执行加法：(+ 1 2)" (+ 1 2))

  (show "5. cond 测试" (cond ((= 1 2) 'wrong)
                             ((= 3 3) 'right)
                             (else 'fallback)))

  (show "6. if 测试" (if #f 'yes 'no))

  (show "7. and 短路测试" (and #t #t #f (display "Hi"))) ; 这里仍然短路，只返回 #f

  (display "8. 强制执行所有表达式：") (newline)
  (show "  a. #t" #t)
  (show "  b. #t" #t)
  (show "  c. #f" #f)
  (display "Hi") (newline))
