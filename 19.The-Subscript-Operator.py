# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18, 2019

File: The Subscript Operator
@author: Byen23

Although a simple for loop can access any of the characters in a string. sometimes you just want to inspect one character at a given position without visiting them all. The subscript operator [] makes this possible. The simplest form of the subscript operation is the following:
	
<a string[<an integer expression>]

The first part of this operation is the string you want to inspect. The integer expression is also called an index. In the following examples, the subscript operator is used to access characters in the string "Alan Turing":
	
"""

name = "Alan Turing"
print(name[0])		 	 	 # Examine the first character

print(name[3])		 	 	 # Examine the fourth character

print(name[len(name) -1])	 # Examine the last character 

print(name[-1])				 # Shorthand for the last character

print(name[-2])			 	 # Shorthand for the next last character 
#-------------------------------------------------------------------#
"""Note that attempting to access a character using a position that equals the string’s length results in an error. 

The positions usually range from 0 to the length minus 1. However, Python allows negative subscript values to access characters at or near the end of a string. The programmer counts backward from –1 to access characters from the right end of the string. The subscript operator is also useful in loops where you want to use the positions as well as the characters in a string. 

The next code segment uses a count-controlled loop to display the characters and their positions: """

data = "Hi there!"
for index in range(len(data)):
	print(index, data[index])

