		

		# |Python Tutorial -53| |Regular Expressions - 2 || Regular Expression methods |


	# findall()
	# search()
	# split()
	# sub()

			# findall()

# import re

# txt = 'I am a ieprasd@gmail.com and hes is xyz@gmail.com'

# y = re.findall('\w+@gmail.com',txt)
# print(y)

# >>>
# ['ieprasd@gmail.com', 'xyz@gmail.com']

# y = re.findall('a\w',txt)
# print(y)
# # >>>
# # ['am', 'as', 'ai', 'an', 'ai']


# y = re.findall('a\w+',txt)
# print(y)
# # >>>
# # ['am', 'asd', 'ail', 'and', 'ail']


# y = re.findall('\wa\w+',txt)
# print(y)

# >>>
# ['rasd', 'mail', 'mail']


# y = re.findall('\w+a\w+',txt)
# print(y)

# >>>
# ['ieprasd', 'gmail', 'gmail']


# y = re.findall('\w*a\w+',txt)
# print(y)

# >>>
# ['am', 'ieprasd', 'gmail', 'and', 'gmail']

	# -----------------------



			# search()

import re

txt = 'Python is a great final language'

# y = re.search('python',txt)
# print(y)

# # >>>
# # None

# y = re.search('Python',txt)
# print(y)

# >>>
# <re.Match object; span=(0, 6), match='Python'>

	
# y = re.search('\wython',txt)
# print(y)

# >>>
# <re.Match object; span=(0, 6), match='Python'>

# y = re.search('\w{5}',txt)
# print(y)

# >>>
# <re.Match object; span=(0, 5), match='Pytho'>


		# ---------------

		# sub()

import re

txt = 'Python is a great final language'

# y = re.sub('\s','@',txt)
# print(y)

# >>>
# Python@is@a@great@final@language


# y = re.sub('\s','@',txt,2)
# print(y)

# >>>
# Python@is@a great final language























