(define (help head tail n)
    (if (null? tail) (cons head nil)
        (if (= n 0) (cons head tail)
            (help (append head (list (car tail))) (cdr tail) (- n 1))
        )
    )
)
(define (split-at lst n)
  'YOUR-CODE-HERE
  (help nil lst n)
)


(define-macro (switch expr cases)
	 (cons 'cond 
	   (map (lambda (x) `((eq? (car ,x) ,expr) (cdr ,x))) cases)
)
)

(switch b ((a (print 'a))
                (b (print 'b))
                (c (print 'c))))
