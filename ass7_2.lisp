(print "Enter the number whose factorial is to be found:")
(defvar  element (read))

(setf fact1 1)
(defun factorial(n)
  (loop for a from 2 to n
        do(setq fact1 (* a fact1))
        )
  ( format t "~% Without  recursion  ~d " fact1)
  )
(factorial element)

(defun fact(n)
  (if (= n 1)
     1
     (* n (fact( - n 1)))
     )
  )
(setq ans (fact element))
( format t "~% With recursion  ~d " ans)

