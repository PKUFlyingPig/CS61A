
(define-macro (def func args body)
    'YOUR-CODE-HERE
    `(define ,(cons func args) ,body)    
)

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))


(define all-three-multiples
  (map-stream (lambda (x) (+ 3 x)) (cons-stream 0 all-three-multiples))
)

(define (compose-all funcs)
  'YOUR-CODE-HERE
  (if (null? funcs) (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))
  )
)

(define (helper ps s)
    (if (null? s) nil
    (cons-stream (+ ps (car s)) (helper (+ ps (car s)) (cdr-stream s)))
))
(define (partial-sums stream)
  'YOUR-CODE-HERE
  (helper 0 stream)
)

