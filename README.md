# 19.The-Subscript-Operator

Although a simple for loop can access any of the characters in a string. 
Sometimes you just want to inspect one character at a given position without visiting them all. 
The subscript operator [] makes this possible. The simplest form of the subscript operation is the following:
	
<a string[<an integer expression>]

The first part of this operation is the string you want to inspect. 
The integer expression is also called an index. In the following examples, 
the subscript operator is used to access characters in the string "Alan Turing":

"""Note that attempting to access a character using a position that equals the string’s length results in an error. 

The positions usually range from 0 to the length minus 
 
 1. However, Python allows negative subscript values to access characters at or near the end of a string. 
  The programmer counts backward from –1 to access characters from the right end of the string. 
  The subscript operator is also useful in loops where you want to use the positions as well as the characters in a string. 

The next code segment uses a count-controlled loop to display the characters and their positions: """
