#! usr/bin/python
from __future__ import division
from sympy import roots

import numpy as np
import random as random
import sympy as sp

"""

give us a degree of a function(1-5)

get a random function with said degree

show the function

find the solution(s) of the function
"""

def function_generator(degree):
	#1 < Degree < 5
	coefficients = [0] * degree
	i = 0
	while i < degree:
		coefficients[i] = random.randint(-10, 10)
		i += 1
		#sets up all coefficients
	
	
	x = sp.symbols('x')
	polynomial = [0]
	
	y = 0
	j = degree + 1
	while y < j:
		print coefficients[y]
		print x**y
		polynomial += coefficients[y] * x**y
		#create the polynomial with degree y
		y += 1
		
	return sp.solve(polynomial, x)
print function_generator(3)
