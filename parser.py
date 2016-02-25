#!/usr/bin/python
# parser.py
# purpose: parse the input after the 
#          lexical analysis
import ply.yacc as yacc

from terms import Variable as Variable
from terms import Application as Application
from terms import Abstraction as Abstraction 

# From documention: write grammar first
# docstrings of methods contain CFG spec
# must use defined tokens or literals
# parser uses shift-reduce parsing
# BACKSLASH and VARIABLE are tokens
# parens are literals
# uppercase == terminals
# lowercase == nonterminals
#
# Program : Term
#
# Term : '(' Term ')'
#      | VARIABLE
#      | Term Term
#      | BACKSLASH VARIABLE '.' Term    

def p_start(p):
		' Program : Term '
		#   p[0]    p[1]
		p[0] = p[1]

def p_paren(p):
		''' Term : '(' Term ')' '''
		#   p[0]    (  p[2]  )
		# since parens are literals
		p[0] = p[2]

def p_variable(p):
		' Term : VARIABLE '
		# p[0]   method on p[1]	  
		p[0] = Variable(p[1])

def p_application(p):
		' Term : Term Term '
		# p[0]   p[1] p[2]
		p[0] = Application(p[1], p[2])

def p_abstraction(p):
		''' Term : BACKSLASH VARIABLE '.' Term '''
		#   p[0]       \  method on p[2] . p[4]
		p[0] = Abstraction(Variable(p[2]), p[4])
    
    
