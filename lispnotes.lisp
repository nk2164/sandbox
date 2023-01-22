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
