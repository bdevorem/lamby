#!/usr/bin/python
# lamby.py
# purpose: shell for interpreter

import sys

# directions from PLY package
import ply.lex as lex
import ply.yacc as yacc

if __name__ == "__main__":
	
	print 'Welcome to Lamby!\nType \'exit\' to exit.'
	
	while(1):
		s = raw_input('> ')
		if s == 'exit':
			sys.exit(0)
        
