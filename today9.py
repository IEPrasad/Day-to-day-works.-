

		# | Python Tutorial -47 | Random Numbers |

		# ********
		# Random numbers in programming refer to values generated unpredictably 
		# or without a discernible pattern. These numbers are typically used for
		# various purposes, such as creating random simulations, games, or 
		# cryptographic applications. Programming languages provide functions or 
		# modules to generate random numbers. It's important to note that these 
		# numbers are not truly random but are generated using algorithms and seeds. 
		# Seeds are initial values that influence the sequence of random numbers 
		# generated, allowing for reproducibility if the same seed is used.


# 1) ------------
			
			# random()

# import random 
# x = random.random()
# print(x)
# # >>> 0.2707167296438441
# # ** run this program few times 
# # when you see the random numbers 


# -----

# import random 
# x = random.random()*10
# print(x)
## if you run this program few times 
# you can see the random numbers 
# >>> run few times 
# 8.147998590381487
# 0.03525057379861862
# 6.726250793919322
# 2.0801694024227357

# ---------

		# uniform() 

# import random
# x = random.uniform(1,10)
# print(x)

# >>> >>> 
# 4.2986253494609405
# 3.3874289413140524
# 4.198160116340234
# 2.1762726715745577

# ---- 

# import random
# x = random.uniform(5,10)
# print(x)

# >>> >>> 
# 9.525546907549927
# 7.660047471796397
# 5.546326158064972
# 6.9725838045455175
		
#-----------
		
			# randint()

# import random
# x = random.randint(2,10)
# print(x)
# >>> >>>
# 2
# 2
# 9
# 10

# ----------------------

			# choice()

# import random
# name = ['Kamal','Nimal','Amal']
# winner = random.choice(name)
# print(winner)

# >>> >>> 
# kamal 
# Nimal
# Nimal
# Amal

#-------------

			# choices()


# import random
# name = ['AB','BC','CD','TR','DF']
# w = random.choices(name,k=2)
# print(w)

# >>> >>>
# ['AB', 'BC']
# ['TR', 'BC']
# ['AB', 'DF']

	# when k = 4 

# import random
# name = ['AB','BC','CD','TR','DF']
# w = random.choices(name,k=4)
# print(w)

# >>> >>>
# ['DF', 'DF', 'CD', 'CD']
# ['CD', 'AB', 'BC', 'AB']
# ['AB', 'TR', 'CD', 'TR']


# --------------------

			# shuffle()


# import random
# numbers = list(range(1,10))
# print(numbers)
# >>>
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ---

# import random
# numbers = list(range(1,10))
# random.shuffle(numbers)
# print(numbers)

# >>>
# [4, 7, 9, 2, 1, 3, 5, 8, 6]
# [9, 8, 2, 6, 1, 4, 3, 5, 7]






