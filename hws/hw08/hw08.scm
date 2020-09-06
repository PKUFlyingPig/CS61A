(define (helper curr num s)
    (if (and (not (null? s)) (= curr (car s))) (helper curr (+ num 1) (cdr-stream s))
        (list curr num)
    )
)

(define (next s curr)
    (if (null? s) nil
    (if (= (car s) curr) (next (cdr-stream s) curr) s
    )
)
)

(define (rle s)
  'YOUR-CODE-HERE
  (if (null? s) nil
    (cons-stream (helper (car s) 0 s) (rle (next s (car s))))
  )
)


(define (helper2 curr s ans)
    (if (and (not (null? s)) (<= curr (car s))) (helper2 (car s) (cdr-stream s) (append ans (list (car s))))
        ans 
    )
)

(define (next2 s curr)
    (if (null? s) nil
    (if (>= (car s) curr) (next2 (cdr-stream s) (car s)) s
    )
)
)
(define (group-by-nondecreasing s)
    'YOUR-CODE-HERE
    (if (null? s) nil
        (cons-stream (helper2 (car s) (cdr-stream s) (list (car s))) (group-by-nondecreasing (next2 s (car s))))
    )   
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

