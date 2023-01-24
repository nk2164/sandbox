;; global variables are defined with the defparameter function.
;; The asterisps '*' are called earmuffs.

(defparameter *small* 1)
(defparameter *big* 100)

;; With - defparameter, if the same variable is defined again, its overwritten.
;; (defparameter *big* 129) - Commented this because i don't want this to mess 
;; with my logic.

;; defvar is another command for declaring global variables.
;; subsequent resetting of value does not changes the value.
(defvar *foo* 20)
(defvar *foo* 10)

;; Defining global functions in lisp.
;; ash does an arithmatic shift .. -1 basically halves the number.
(defun guess-my-number()
    (ash (+ *small* *big*) -1))

;; if the user, replies small, then you need to reset big to 1 - that number
;; which just displayed.
(defun small()
   (setf *big* (1-(guess-my-number)))
   (guess-my-number))

;; if the user, replies large, then you need to reset small to 1 + that number
;; which just displayed.  
(defun big()
   (setf *small* (1+(guess-my-number)))
   (guess-my-number))

;; start-over, basically resets the values of small and big..then calls the game
;; again.
(defun start-over()
       (defparameter *small* 1)
       (defparameter *big* 100)
       (guess-my-number))

;; Defining local vars in lisp.
(let ((a 5)
      (b 6))
   (+ a b))

;; Defining local functions...using flet statement.
(flet ((f (n)
          (+ n 10)))
      (f 5))

;; eq builtin
(eq 'foo 'foo)

;; calculating exponential
(expt 2 2)

;; symbols are case insensitive. The below
;; code would give True(T)
(eq 'Foo 'foo)

;; displaying string - can include escaped chars as well.
(princ "Tutti Frutti")
(princ "He yelled \"Stop that thief!\" from the busy street.")

;; The code mode is default...which is function followed by form
;; You need to preface with a ' if you need to treat it like data.This is 
;; called quoting.
(expt 2 3)  ;; This is interpreted in code mode and returns an 8
'(expt 2 3) ;; This is interpreted in data mode. This would just treat
            ;; it like a string and return it back.

;; cons cell they are like a glue that holds all the lists
;; together. 

;; Lists in lisp are manipulated using cons cdr and car

(cons 'pork' '(beef chicken))
