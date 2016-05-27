# b_reduction.py
# purpose: to reduce parsed lambda calc redex
# into normal form

from parsing_objects import Variable as Variable
from parsing_objects import Application as Application
from parsing_objects import Abstraction as Abstraction

def recursive_substitution(old, substituter, new):
	# Variable
	# check if substituter matches var
	if isinstance(old, Variable):
		if old._name == substituter._name:
			return new
            
  # Application
  # since Application : Term Term, recurse on both 
  # terms to eventually get to Variable case above
	elif isinstance(old, Application):
		old._first = recursive_substitution(old._first, substituter, new)
		old._second = recursive_substitution(old._second, substituter, new)

	# Abstraction
	# if the variable in the abstraction matches the substituter,
	# want to get to Variable case above
	# else, recurse on body for same reason
	elif isinstance(old, Abstraction):
		if old._variable == substituter:
			old._variable = recursive_substitution(old._variable, substituter, new)
		old._body = recursive_substitution(old._body, substituter, new)

	return old


def beta_reduce(term):

	# inner function to recursively reduce until a Variable or
	# Abstraction is reached, following the steps lined out in
	# http://www.cs.yale.edu/homes/hudak/CS201S08/lambda.pdf
	
	def recursive_reduce(t):
		if isinstance(t, Variable) or isinstance(t, Abstraction):
			return t

		elif isinstance(t, Application):
			if isinstance(t._first, Abstraction):
				return recursive_substitution(t._first._body,
													t._first._variable,
													t._second)
			else:
				# recurse on first element of Application until
				# it is fully reduced, then move on to second element
				new_first = recursive_reduce(t._first)
				if new_first != t._first:
					t._first = new_first
					return t
				else:
					t._second = recursive_reduce(t._second)
					return t
		

	if isinstance(term, Variable) or isinstance(term, Abstraction):
		# no reduction to be done
		return term
	elif isinstance(term, Application): #needs to be reduced
		tmp_term = term

		while(True):
			term_str = str(tmp_term) #objectify term
			reduced_term = recursive_reduce(tmp_term)
			reduced_term_str = str(reduced_term)

			if term_str == reduced_term_str:
				# if fully reduced
				return tmp_term
			else:
				# continue on if theres more to do
				tmp_term = reduced_term
                
                
