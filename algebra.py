#! usr/bin/python
from __future__ import division
from sympy import roots

import numpy as np
import random as random
import sympy as sp
import re as re

"""

give us a degree of a function(1-5)

get a random function with said degree

show the function

find the solution(s) of the function
""" 

class make_pretty_polynomial():
# 	def repr(argh):
# 		polynomial.replace("*"\*, "*")
# 			

	def function_generator(degree):
		#1 <= Degree <= 4
		loop_degree = degree + 1 #loop_degree is incremented by one just so in our loop, we get the correct degree output.
		coefficients = [0] * loop_degree
		first_counter = 0
		while first_counter < loop_degree:
			coefficients[first_counter] = random.randint(-10, 10)
			first_counter += 1
			if coefficients[degree] == 0:
				first_counter = 0
				coefficients = [0] * loop_degree
			print coefficients
			#sets up all coefficients and doesn't allow for the leading coefficient to be 0
		x = sp.symbols('x')
		polynomial = 1
		second_counter = 0
		while second_counter < loop_degree:
			polynomial += coefficients[second_counter] * x**second_counter
			#create the polynomial with degree "second_counter"
			second_counter += 1
		
		exact_solution = sp.solve(polynomial, x)
		pretty_polynomial = re.sub('\*\*', '^', str(polynomial))
		prettier_polynomial = re.sub('\*', '', str(pretty_polynomial))
		print "The solutions to polynomial " + prettier_polynomial + " with random coefficients and a degree of " + str(degree) + " is: "
		
		# for solution in exact_solution:
# 			approximate_solution[solution] = sp.N(exact_solution[solution], 3)
# 		print approximate_solution
		
		counter = 0
		approximate_solution = exact_solution
		#re.search('\I', )
		for solution in exact_solution:
			to_float = complex(solution)
			approximate_solution[counter] = to_float
			counter = counter + 1
			print approximate_solution 
		
	#	if exact_solution = []
		'There is no real solution, but the complex solutions are'
			
		"""
		
		We want to:
		-change expression of exact_solution to a string so that we can operate the simpify method
		-Get rid of complex solutions
		-if not real solutions, say so
		
		"""
		#return approximate_solution
	print function_generator(3)
