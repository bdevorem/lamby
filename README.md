Lamby 
=====

A Lambda Calculus interpreter, written in Python.

##Usage
###To start the interpreter:
	python lamby.py
###To interpret an expression:
	[expression] + ENTER
###To quit:
	exit

##Examples
$ python lamby.py
Welcome to Lamby!
Type 'exit' to exit.
> (\x.x)
Reduced expression -> (\x.x)
> (\x.3)5
Reduced expression -> 3
> (\x.x)a
Reduced expression -> a
> a(\x.x)b(\y.y)a
Reduced expression -> aba
> exit
$

TO DO:
- [x] intepreter shell
- [x] lexer
- [x] beta reduction
- [x] parser
- [ ] primitive functionality
- [ ] arithmetic functionality
