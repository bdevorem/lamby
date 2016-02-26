Lamby 
=====

A Lambda Calculus reducer, written in Python.  
Shorthand is not supported.  
Future work: turn the reducer into an interpreter, 
supporting numbers and arithmetic.  

##Usage
###Semantics:
	lambda == \  
	variables == a-z or 0-9  
	lambda abstraction == \ variable . body  
	
###To start the interpreter:
	python lamby.py
###To interpret an expression:
	[expression] + ENTER
###To quit:
	exit

##Examples
>$ python lamby.py  
>Welcome to Lamby!  
>Type 'exit' to exit.  
\> (\x.x)  
Reduced expression -> (\x.x)  
\> (\x.3)5  
Reduced expression -> 3  
\> (\x.x)a  
Reduced expression -> a  
\> a(\x.x)b(\y.y)a  
Reduced expression -> aba  
\> exit  
>$  

##To Do
- [x] intepreter shell
- [x] lexer
- [x] beta reduction
- [x] parser
- [ ] primitive functionality
- [ ] arithmetic functionality

##Sources
http://www.itu.dk/people/sestoft/lamreduce/
http://www.dabeaz.com/ply/ply.html#ply_nn22
http://www.inf.fu-berlin.de/lehre/WS03/alpi/lambda.pdf
http://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html
https://en.wikipedia.org/wiki/Lambda_calculus
http://www.cs.yale.edu/homes/hudak/CS201S08/lambda.pdf

