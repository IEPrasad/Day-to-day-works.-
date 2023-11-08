

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



		














