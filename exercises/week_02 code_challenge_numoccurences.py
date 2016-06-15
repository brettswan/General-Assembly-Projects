'''
Wednesday Morning Challenge

Question: 
The numberOfOccurrences function must return the number of occurrences of an element in an array.

Example: 
sample = [0,1,2,2,3]
number_of_occurrences(0) == 1
number_of_occurrences(4) == 0
number_of_occurrences(2) == 2
number_of_occurrences(3) == 1

Starter code:

def number_of_occurrences(sample, xs)
	pass 

'''
#Method 1
def number_of_occurrences(s, xs):
    total = 0
    for x in xs:
        if x == s:
            total+=1
    return total

#Method 2
def number_of_occurrences(s, xs):
    return xs.count(s)

#Method 3

def number_of_occurrences(s, xs):
    return sum(s == y for y in xs)

#Method 4 - helper package collections

from collections import Counter
def number_of_occurrences(s, xs):
    return Counter(xs)[s]

#Method 5 - lambda functions
def number_of_occurrences(s, xs):
    equalsS = lambda x: x == s  
    return len(filter(equalsS ,xs))

# If time introduction assertions
# conda install or pip install pytest
import pytest 

assert 