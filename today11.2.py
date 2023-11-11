

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

import re 

# 1) \ back slash 

				definition 				examples
										
		\d 		0-9						'3', '1', '0', '6' ,'9' .. 
		\w     	A-Z, a-z, 0-9			'8', '4', 'e', 'R', 't' ..
		\W 		not \w 					' ', '@', '?', '$' ..
		\s 		white space 			' '
		\S 		not \s 					'6', 'n', 'A', '@', 'T', '3'..










