

		# |Python Tutorial -49|| Pyramid | |Half Pyramid|


		# *** In programming, a "pyramid" often refers to a design pattern or structure 
		# in code where each layer or level represents a different abstraction or 
		# functionality. The term can be used in various contexts, such as software 
		# architecture, testing, or even in graphical user interfaces. For example, 
		# in a testing pyramid, different types of tests (unit tests, integration tests, 
		# and end-to-end tests) form layers with different scopes and responsibilities.
		# The concept of a pyramid is a metaphorical way to illustrate the recommended 
		# distribution and balance of different components or practices in a system or 
		# project.



# n = 5
# for i in range(n):
# 	for j in range(i+1):
# 		print('* ',end="")

# 	print()

# >>>
# *
# * *
# * * *
# * * * *
# * * * * *


# -----------

# n = 5
# for i in range(n):
# 	for j in range(n-i):
# 		print('* ',end="")
# 	print()

# >>>
# * * * * *
# * * * *
# * * *
# * *
# *


# ---------------

n = 5
for i in range(n):
	for j in range(n-i-1):
		print(' ',end=" ")
	for k in range(2*i+1):	
		print("* ",end="")
	print()

>>>>
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *













