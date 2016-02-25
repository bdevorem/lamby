#!/usr/bin/python
# lexer.py
# purpose: lexer for user input, implemented
#          with PLY package

import ply.lex as lex
from ply.lex import LexError
import re

# List of token names. This is always required
# ^^ from PLY documentation
tokens = [
		'LPAREN',
		'RPAREN',
		'VARIABLE',
		'BACKSLASH' # represents lambda
]

# Character that are returned "as is" when 
# encountered by the lexer
literals = ['\\', '(', ')', '.']

# Regular expression rules for simple tokens
# parens are unnecessary
t_VARIABLE = r'[a-z]'
t_BACKSLASH = r'\\'

# Error handling rule, straight from documentation
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

