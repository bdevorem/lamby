# parsing_objects.py
# purpose: make life easier
#          When the parser follows the grammar
#          and breaks up input into what the
#          lambda calc string is, these objects
#          allow for easier computations between
#          different calc functionalities


class Variable (object):
	def __init__ (self, name):
			self._name = name

	def __str__ (self):
			return str(self._name)

	def __eq__ (self, other):
		# two variables are the same if they are the same character
		if isinstance (other, Variable):
			if other._name == self._name:
				return True
		return False
        
	def normalform(self):
		# one of the rules of Lambda Calc
		return True

class Application (object):
	def __init__ (self, first, second):
		self._first = first
		self._second = second

	def __str__ (self):
		#if isinstance(self._second, Abstraction):
		#	if self._second._identity is True:
		#		return str(self._first)
	
		return str (self._first) + str (self._second)

	def __eq__ (self, other):
	# same as above, but two variables combined
		if isinstance (other, Application):
			return (other._first == self._first) and \
             (other._second == self._second)
		return False

	def normalform(self):
		# def not normal form. Lambda calc rules.
		if isinstance(self._first,Abstraction) :
			return False
		elif isinstance(self._first,Application) :
			return self._first.normalform()
		else:
			return True

class Abstraction (object):
	def __init__ (self, variable, body):
		self._variable = variable
		self._body = body
		
		if self._variable == self._body:
			self._identity = True
		else:
			self._identity = False
			
		if isinstance(self._body, Abstraction):
			if self._body._identity is True:
				pass
				
	def __str__ (self):
		return '(\\' + str(self._variable) + '.' + str(self._body) + ')'

	def __eq__ (self, other):
		if isinstance (other, Abstraction):
			return (other._variable == self._variable) and \
             (other._body == self._body)
		return False

	def normalform(self):
		return True

