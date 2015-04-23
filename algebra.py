#! usr/bin/python
from __future__ import division

import numpy as np
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
	j = degree
	while i < degree:
		coefficients[i] = random.randint(-10, 10)
		i += 1
		#sets up all coefficients
	
	
	x = sp('x')
	solve()
	
	
	
	
	