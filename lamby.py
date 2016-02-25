#!/usr/bin/python
# lamby.py
# purpose: shell for interpreter

import sys

# directions from PLY package
import ply.lex as lex
import ply.yacc as yacc

from lexer import *
from parser import *

from algorithms import multi_step_beta_reduce

if __name__ == "__main__":
	lexer = lex.lex()
	parser = yacc.yacc()
	
	print 'Welcome to Lamby!\nType \'exit\' to exit.'
	
	while(1):
		s = raw_input('> ')
		if s == 'exit':
			sys.exit(0)
       
		term = parser.parse(s)
		
		print term
       
