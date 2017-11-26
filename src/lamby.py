#!/usr/bin/python
# lamby.py
# purpose: shell for interpreter

import sys

# import GNU readline library to greatly improve raw_input() prompt
import readline

# directions from PLY package
import ply.lex as lex
import ply.yacc as yacc

from lexer import *
from parser import *

from b_reduction import beta_reduce

if __name__ == "__main__":
	lexer = lex.lex()
	parser = yacc.yacc()
	
	print 'Welcome to Lamby!\nType \'exit\' to exit.'
	
	while(1):
		s = raw_input('> ')
		if s == 'exit':
			sys.exit(0)
		elif s == '':
			pass
		else:
			term = parser.parse(s)
			reduced_term = beta_reduce(term)
			print 'Reduced expression -> ' + str(reduced_term)
       
