(define (repeat k fn)
  (fn)
  (if (> k 1) (repeat (- k 1) fn)))

(define (tri fn)
  (repeat 3 (lambda () (fn) (lt 120))
