

	# | Python Tutorial -52| |Regular Expression -1 | | Metacharacters | 


		# ** 
		# Regular expressions, often referred to as regex or regexp, are powerful sequences 
		# of characters that define a search pattern. They are used for pattern matching 
		# within strings, enabling sophisticated text search and manipulation operations. 
		# Metacharacters are special characters in a regular expression that have a special 
		# meaning, and they are used to define the rules or patterns for matching. Examples 
		# of metacharacters include . (dot), * (asterisk), + (plus), ? (question mark), [] 
		# (square brackets), () (parentheses), and more. Metacharacters allow you to express 
		# complex search patterns by representing character classes, repetitions, alternatives, 
		# and other rules within a regular expression. Understanding metacharacters is crucial 
		# for effectively using regular expressions in tasks such as text searching, validation, 
		# and data extraction.



# ----------------------

		# Metacharacters

		# \ signals a special sequence 
		# [] a set of characters
		# . any character
		# ^ start with 
		# $ ends with
		# * zero or more occurrences 	
		# + one or more occurrences
		# {} exactly the specified number of occurrences

# ----------------------
1# 1) \ back slash 

# 				definition 				examples
										
# 		\d 		0-9						'3', '1', '0', '6' ,'9' .. 
# 		\w     	A-Z, a-z, 0-9			'8', '4', 'e', 'R', 't' ..
# 		\W 		not \w 					' ', '@', '?', '$' ..
# 		\s 		white space 			' '
# 		\S 		not \s 					'6', 'n', 'A', '@', 'T', '3'..
#		. 		all 					all characters 



# import re

# ##$ re.findall() mehtod

# str = 'Hello Ben10 ?'
# y = re.findall('\d',str)
# print(y)

# # >>>
# # ['1', '0']

# str = 'Hello Ben10 ?'
# y = re.findall('\w',str)
# print(y)

# # >>>
# # ['H', 'e', 'l', 'l', 'o', 'B', 'e', 'n', '1', '0']

# str = 'Hello Ben10 ?'
# y = re.findall('\W',str)
# print(y)

# # >>>
# # [' ', ' ', '?']

# str = 'Hello Ben10 ?'
# y = re.findall('\s',str)
# print(y)

# # >>>
# # [' ', ' ']

# str = 'Hello Ben10 ?'
# y = re.findall('\S',str)
# print(y)

# # >>>
# # ['H', 'e', 'l', 'l', 'o', 'B', 'e', 'n', '1', '0', '?']

# str = 'Hello Ben10 ?'
# y = re.findall('.',str)
# print(y)

# # >>>
# # ['H', 'e', 'l', 'l', 'o', ' ', 'B', 'e', 'n', '1', '0', ' ', '?']


# str = 'Hello Ben10 ?'
# y = re.findall('\w\w\w\w\w',str)
# print(y)

# # >>>
# # ['Hello', 'Ben10']

# str = 'Hello Ben10 ?'
# y = re.findall('\w\w\w\d\d',str)
# print(y)

# # >>>
# # ['Ben10']

#----------------------------------


	# {n}  			exat n occurrences
	# {min, max}		min-max occurrences
	# * 				0 or more occurrences
	# + 				1 or more occurrences
	# ? 				0 or 1 occurrences

 	

# import re

# str = 'hello ben10 ?'
# y = re.findall('\w{3}\d{2}',str)
# print(y)

# # >>>
# # ['ben10']

# str = 'hello ben10 ?'
# y = re.findall('\w{3}',str)
# print(y)

# # >>>
# # ['hel', 'ben']

# str = 'hello ben10 ?'
# y = re.findall('\w{2,3}',str)
# print(y)

# # >>>
# # ['hel', 'lo', 'ben', '10']

# str = 'hello ben10 ?'
# y = re.findall('\w+',str)
# print(y)

# # >>>
# # ['hello', 'ben10']

# str = 'hello ben10 ?'
# y = re.findall('\w*',str)
# print(y)

# # >>>
# # ['hello', '', 'ben10', '', '', '']

# str = 'hello ben10 ?'
# y = re.findall('\w?',str)
# print(y)

# # >>>
# # ['h', 'e', 'l', 'l', 'o', '', 'b', 'e', 'n', '1', '0', '', '', '']

# ------------------------


		# ^ start with 
		# $ end with 


import re

str = 'hello ben10 ?'
y = re.findall('^\w+', str)
print(y)

# >>>
# ['hello']

str = 'hello ben10 ?'
y = re.findall('^\w+$', str)
print(y)

# >>>
# []

str = 'hello ben10 ?'
y = re.findall('\w+$', str)
print(y)

# >>>
# []



str = 'hello welcome'
y = re.findall('\w+$', str)
print(y)

>>>
['welcome']










