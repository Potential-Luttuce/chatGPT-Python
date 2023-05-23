# Task 4
# Fibonacci Series: Write a program to generate the Fibonacci sequence 
# up to a specified number of terms. The Fibonacci sequence starts with 0 and 1,
#  and each subsequent number is the sum of the two preceding numbers.

import os
from functions import *

os.system('clear && neofetch')

global terms
terms = getTerms()
getFib(terms)
