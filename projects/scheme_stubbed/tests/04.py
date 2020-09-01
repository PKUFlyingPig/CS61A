test = {
  'name': 'Problem 4',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          #t
          scm> (and 1 #f)
          #f
          scm> (and (+ 1 1) 1)
          1
          scm> (and #f 5)
          #f
          scm> (and 4 5 (+ 3 3))
          6
          scm> (and #t #f 42 (/ 1 0))
          #f
          scm> (not (and #f))
          #t
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (and 3 2 #f)
          #f
          scm> (and 3 2 1)
          1
          scm> (and 3 #f 5)
          #f
          scm> (and 0 1 2 3)
          3
          scm> (define (true-fn) #t)
          true-fn
          scm> (and (true-fn))
          #t
          scm> (define x #f)
          x
          scm> (and x #t)
          #f
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          x
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      #f
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          #f
          scm> x
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (and #t #t #t #t))
          no-mutation
          scm> no-mutation
          (lambda () (and #t #t #t #t))
          scm> (no-mutation)
          #t
          scm> no-mutation ; `and` should not cause mutation
          (lambda () (and #t #t #t #t))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (or)
          #f
          scm> (or (+ 1 1))
          2
          scm> (not (or #f))
          #t
          scm> (define (t) #t)
          t
          scm> (or (t) 3)
          #t
          scm> (or 5 2 1)
          5
          scm> (or #f (- 1 1) 1)
          0
          scm> (or 4 #t (/ 1 0))
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (or 0 1 2)
          0
          scm> (or 'a #f)
          a
          scm> (or (< 2 3) (> 2 3) 2 'a)
          #t
          scm> (or (< 2 3) 2)
          #t
          scm> (define (false-fn) #f)
          false-fn
          scm> (or (false-fn) 'yay)
          yay
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          #f
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     #t
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          #t
          scm> x
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (or #f #f #f #f))
          no-mutation
          scm> no-mutation
          (lambda () (or #f #f #f #f))
          scm> (no-mutation)
          #f
          scm> no-mutation ; `or` should not cause mutation
          (lambda () (or #f #f #f #f))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (greater-than-5 x) (if (> x 5) #t #f))
          greater-than-5
          scm> (define (other y) (or (greater-than-5 y) #f))
          other
          scm> (other 2)
          #f
          scm> (other 6) ; test for mutation
          #t
          scm> (define (other y) (and (greater-than-5 y) #t))
          other
          scm> (other 2)
          #f
          scm> (other 6) ; test for mutation
          #t
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       ((< 2 5) 7)
          ....       (else 8))
          7
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       (else 8))
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (if 0 1 2)
          1
          scm> (if #f 1 (if #t 2 3))
          2
          scm> (if (= 1 2) (/ 1 0) 'a)
          a
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       ((< 2 5) 7))
          7
          scm> (cond ((> 2 3) (display 'oops) (newline))
          ....       (else 9))
          9
          scm> (cond ((< 2 1))
          ....       ((> 3 2))
          ....       (else 5))
          #t
          scm> (cond (#f 1))
          scm> (cond ((= 4 3) 'nope)
          ....       ((= 4 4) 'hi)
          ....       (else 'wat))
          hi
          scm> (cond ((= 4 3) 'wat)
          ....       ((= 4 4))
          ....       (else 'hm))
          #t
          scm> (cond ((= 4 4) (+ 40 2))
          ....       (else 'wat 0))
          42
          scm> (cond (12))
          12
          scm> (cond ((= 4 3))
          ....       ('hi))
          hi
          scm> (eval (cond (False 1) (False 2)))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cond (0 'yea)
          ....       (else 'nay))
          yea
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (define y 0)
          y
          scm> (define z 0)
          z
          scm> (cond (#t
          ....        (define x (+ x 1))
          ....        (define y (+ y 1))
          ....        (define z (+ z 1)))
          ....       (else
          ....        (define x (- x 5))
          ....        (define y (- y 5))
          ....        (define z (- z 5))))
          z
          scm> (list x y z)
          (1 1 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (print-and-false val)
          ....         (print val)
          ....         #f)
          print-and-false
          scm> (cond ((print-and-false 'cond1))
          ....       ((print-and-false 'cond2))
          ....       ((print-and-false 'cond3))
          ....       ((print-and-false 'cond4)))
          cond1
          cond2
          cond3
          cond4
          scm> (define (print-and-true val)
          ....         (print val)
          ....         #t)
          print-and-true
          scm> (cond ((print-and-false 'cond1))
          ....       ((print-and-false 'cond2))
          ....       ((print-and-true 'cond3))
          ....       ((print-and-false 'cond4)))
          cond1
          cond2
          cond3
          #t
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 1)
          x
          scm> (let ((x 5))
          ....    (+ x 3))
          8
          scm> x
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (let ((a 1) (b a)) b)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (let ((x 5))
          ....    (let ((x 2)
          ....          (y x))
          ....        (+ y (* x 2))))
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> (define (f x y)
          ....    (let ((a (+ 1 (* x y)))
          ....          (b (- 1 y)))
          ....        (+ (* x (square a))
          ....           (* y b)
          ....           (* a b))))
          f
          scm> (f 3 4)
          456
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 3)
          x
          scm> (define y 4)
          y
          scm> (let ((x (+ y 2))
          ....       (y (+ x 2)))
          ....      (cons x (cons y nil)))
          (6 5)
          scm> (let ((x 'hello)) x)
          hello
          scm> (let ((a 1) (b 2) (c 3)) (+ a b c))
          6
          scm> (define z 0)
          z
          scm> (let ((a (define z (+ z 1)))) z)
          1
          scm> (let ((x 1)
          ....       (y 3))
          ....    (define x (+ x 1))
          ....    (list x y))
          (2 3)
          scm> (let ((a 1 1)) a)
          SchemeError
          scm> (let ((a 1) (2 2)) a)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define y 1)
          y
          scm> (define f (mu (x) (+ x y)))
          f
          scm> (define g (lambda (x y) (f (+ x x))))
          g
          scm> (g 3 7)
          13
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define h (mu () x))
          h
          scm> (define (high fn x) (fn))
          high
          scm> (high h 2)
          2
          scm> (define (f x) (mu () (lambda (y) (+ x y))))
          f
          scm> (define (g x) (((f (+ x 1))) (+ x 2)))
          g
          scm> (g 3)
          8
          scm> (mu ())
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
