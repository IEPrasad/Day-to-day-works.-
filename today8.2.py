

		# |Python Tutorial -46||File Handiling| |OS Module|


# 1- How to import a file 
	
# *** -------------
# x = open('testFor8.2.txt','r')
# print(x.read())								

# >>>
# Taking Snap shots
# Initializing a repository
# Git workflow
# Staging files
# Committing changes
# Committing best practices
# Skipping the staging area
# Removing files
# Removing or moving files
# Ignoring files
# Short status
# Viewing the stage and unstage files

	# 		-------
		
	# 	'r' = read only
	# 	'w' = write only
	# 	'a'	= append
	# 	'w+'= read and write 

	# 		-------



		# |read mode |

# *** -------------------

# x = open('testFor8.2.txt','r')
# print(x.readline())								

# >>>
# Taking Snap shots

# # *** ------------------
# x = open('testFor8.2.txt','r')
# print(x.readline())
# print(x.readline())
# print(x.readline())										

# >>>
# Taking Snap shots

# Initializing a repository

# Git workflow


# *** ----------------
# x = open('testFor8.2.txt','r')
# print(x.readline(),end="")
# print(x.readline(),end="")
# print(x.readline())										

# >>>
# Taking Snap shots
# Initializing a repository
# Git workflow


# *** readline -----> readlines
# x = open('testFor8.2.txt','r')
# print(x.readlines())

# >>>
# ['Taking Snap shots \n', 'Initializing a repository \n', 'Git workflow \n', 'Staging files\n', 'Committing changes \n', 'Committing best practices\n', 'Skipping the staging area \n', 'Removing files \n', 'Removing or moving files \n', 'Ignoring files \n', 'Short status\n', 'Viewing the stage and unstage files\n']


# *** $$ when we open the file we must close this files
	# we can use this for that 

# x = open('testFor8.2.txt','r')
# print(x.readline())
# x.close()
	
	## We need to do this for all open files ...

	## so we can do it another way

# with open('testFor8.2.txt','r') as x:
# 	print(x.read())

# >>>
# Taking Snap shots
# Initializing a repository
# Git workflow
# Staging files
# Committing changes
# Committing best practices
# Skipping the staging area
# Removing files
# Removing or moving files
# Ignoring files
# Short status
# Viewing the stage and unstage files

## When we out the with block it was already closed 

# **** --------------------


			|write mode|


# x = open('testFor8.2.txt','w')
# x.write('Hello World!')
# # we must close it now
# x.close()

# ** be carefull with that 
# 	** because now all of details are remove from testFor8.2 file and
# 		now it has only 'Hello World!'
# 		## remember these
	
	# testFor8.2 file 

	# 	Hello World!
		
# 	# -------------
# x = open('testFor8.2.txt','w')
# x.write('Hello World!')
# x.write('Welcome')
# x.close()

	# now testFor8.2 file has

# 		Hello World!Welcome

# we can fix these problem using 
# 	we can get these in new line using by newline charactor 

# x = open('testFor8.2.txt','w')
# x.write('Hello World!\n')
# x.write('Welcome')
# x.close()

# 	# now testFor8.2 file has

# 		Hello World!
# 		Welcome

# x = open('testFor8.2.txt','w')
# x.write('Hello World!\n \n')
# x.write('Welcome')
# x.close()

# 	# now testFor8.2 file has	

# 		Hello World!
 
# 		Welcome


	# ---------------------

	# **** if you want to let before things 
	#  	you can use || append || mode

				# |append mode|


# 	if testFor8.2.txt file has
# 		Name = Sumathipala
# 		Age = 50

# x = open('testFor8.2.txt','a')
# x.write('hello Sumathi')
# x.close()

# >> now it has testFor8.2.txt file
# 		Name = Sumathipala
# 		Age = 50
# 		hello Sumathi



# x = open('testFor8.2.txt','a')
# x.write('hello Sumathi')
# x.close()

# >>> these file has now 
# 		Name = Sumathipala
# 		Age = 50
# 		hello Sumathihello Sumathi

# ** we can use the new line charactor with like this

# x = open('testFor8.2.txt','a')
# x.write('\nhello Sumathi')
# x.close()

# ** now this file has 
# Name = Sumathipala
# Age = 50
# hello Sumathihello Sumathi
# hello Sumathi

# -----------------------------

# x = open('hello.txt','a')
# **** if there is not hello.txt file but it is auto created now ***

# -----------------

# ** how to open image -------
# x = open('nature.JPG','rb')
# print(x.read())
# 	## rb = readin binary 
# >>> image eka open wenne binary akarayen we


# -----------------------------------------------------------------------------------
	
				# |OS module|

import os


## (1) how to remove a file 
# os.remove('hello.txt')

### now the hello.txt file is removed 


## (2) how to rename a file
# os.rename('before_name','new_name')


## (3) how to know if this file exists 
	# මෙම ගොනුව තිබේදැයි දැන ගන්නේ කෙසේද
# print(os.path.exists('test.txt'))

	## you can show the out put is True or False

## (4) how to find the path of file
# print(os.path.abspath('test.py'))


## (5) how to know the size of file
# print(os.path.getsize('today8.2.py'))	
# >>> 5077 

	## 5077 is the number of element of these file

	





		














