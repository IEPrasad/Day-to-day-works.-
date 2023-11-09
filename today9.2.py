
		# |Python Tutorial -48||Zip Function|


	# *****
		# The zip() function in Python is used to combine elements from two or more 
		# iterables (e.g., lists, tuples) into tuples. It pairs up corresponding elements 
		# based on their positions and creates an iterable of these tuples. The resulting 
		# iterable can be converted to a list or used directly in a loop. If the input 
		# iterables are of different lengths, zip() stops creating tuples when the 
		# shortest input iterable is exhausted. This function is handy for iterating over 
		# multiple sequences simultaneously.

# names = ['Kmal','Saman','Nimal']
# age = [45,12,34]
# details = zip(names,age)
# print(details)

# >>>
# <zip object at 0x0000019F96159840>

	# so we have to take this in the right way
	# we have to get this like a tuple, list, or set 

# names = ['Kmal','Saman','Nimal']
# age = [45,12,34]
# details = list(zip(names,age))
# print(details)

# >>> 
# [('Kmal', 45), ('Saman', 12), ('Nimal', 34)]


	
# names = ['Kmal','Saman','Nimal']
# age = [45,12,34]
# details = tuple(zip(names,age))
# print(details)

# >>>
# (('Kmal', 45), ('Saman', 12), ('Nimal', 34))


# names = ['Kmal','Saman','Nimal']
# age = [45,12,34]
# details = set(zip(names,age))
# print(details)

# >>>
# {('Saman', 12), ('Nimal', 34), ('Kmal', 45)}

		## *** that is very important to know 
			# The elements of the set are not in the order $$$$

		# ------------


		### We can take these out put just like a dictionary 

# names = ['Kmal','Saman','Nimal']
# age = [45,12,34]
# details = dict(zip(names,age))
# print(details)

# >>> 
# {'Kmal': 45, 'Saman': 12, 'Nimal': 34}


# --------------------------

# names = ['Kmal','Saman','Nimal']
# age = [45,12,34]
# marks = [66,77,85]
# details = dict(zip(names,age,marks))
# print(details)

# >>>
# ValueError: dictionary update sequence element #0 has length 3; 2 is required
	## because dictionary only have key and value

# names = ['Kmal','Saman','Nimal']
# age = [45,12,34]
# marks = [66,77,85]
# details = list(zip(names,age,marks))
# print(details)

# >>>
# [('Kmal', 45, 66), ('Saman', 12, 77), ('Nimal', 34, 85)]
	

# -------------------------------------

			# how to unzip zip file

names = ['Kmal','Saman','Nimal']
age = [45,12,34]
marks = [66,77,85]
details = list(zip(names,age,marks))
print(details)

unzip = list(zip(*details))
# unzip is variable name we use any name for that 
print(unzip)

>>>
[('Kmal', 45, 66), ('Saman', 12, 77), ('Nimal', 34, 85)]
[('Kmal', 'Saman', 'Nimal'), (45, 12, 34), (66, 77, 85)]








