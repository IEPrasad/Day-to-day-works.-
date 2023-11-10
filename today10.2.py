
		# | Python Tutorial -50 || Heart Shape |

# for row in range (6):
# 	print(row)
# >>>
# 0
# 1
# 2
# 3
# 4
# 5	

# for row in range (6):
# 	for column in range	(7):
# 		print('*',end="")
# 	print()
# >>>>
# *******
# *******
# *******
# *******
# *******
# *******

## now we have 6 row and 7 columns 

# ---------
		
		
#	 0 1 2 3 4 5 6 7  
#	0  * *    * * 
#	1*     *      *
#	2*            *
#	3  *	    *
#	4    *    *
#	5      *
	

# so we want to get these patten
# let's try to do it 	

for row in range (6):
	for column in range(7):
		if row == 0 and column%3 != 0:
			print(' *',end="")
		elif row == 1 and column%3 ==0:
			print(' *',end="")
		elif row-column == 2:
			print(' * ',end="") 
		elif row+column == 8:
			print('* ',end="")
		else:
			print('  ',end="")
	print()

# >>>	

   * *   * *
 *     *     *
 *           *
   *       *
     *   *
       *


##$$$$ look at these every step 
# $$$$$$$$$$$$$$$$


