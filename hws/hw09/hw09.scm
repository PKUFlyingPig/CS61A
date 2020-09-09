(define (reverse lst)
    'YOUR-CODE-HERE
    (if (null? lst) nil
        (append (reverse (cdr lst)) (list (car lst)))
    )
)

