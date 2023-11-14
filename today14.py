
	|Python Tutorial 56|
		|Import own Modules and packages ( __init__.py )|

What is the module in Python 
		** A Python module can be a simple python file
			calculator.py
			calculator is the module name 

What is the Python package 
		** A Python package can be a collection of different Python modules 
			with an __init__.py File
----------------------

We create a folder in desktop 
Now it is open through vscode using cmd
			code .

and make a python file ex: app.py
and also make a another python file : calculator.py
	

calculator.py file >>
	
def add(num1, num2):
	print(num1+num2)


app.py ---->> 

import calculator

calculator.add(2,4)

# >> run this python file
# >>> 6

print(type(calculator))
# >>> <class 'module'>

------------------- 


we can import this python modules another way

from calculator import add

# ** now we can call directly these add function 

add(2,4)
# >>> 
# 6 

print(type(add))
# >>>
# <class 'function'>

--------------- 
now we can create a anothe function in calculator module

calculator.py --->>

def add(num1,num2):
	print(num1+num2)

def sub(num1,num2):
	print(num1-num2)

app.py ------->>

from calculator import add
from calculator import sub

add(2,4)
sub(10,8)	

# >>>
# 6
# 8

--------- we can do it like these if we want -->>

from calculator import * 

add(3,4)
sub(3,1)

# >>>
# 6
# -1

----
we have to make another file in this folder
	sum_text.py

sum_text.py--->>

def add(txt1, txt2):
	print(f'{txt1}{txt2}')

app.py ------>>

from sum_text import *


## now calculator.py file and sum_text.py has the same function names

# now we can see what happen

add(2, 4)
# >>> 
24

------- we can solve this problem like this

app.py ----->>

from calculator import add as add_num
from sum_text import add ass add_txt

add_num(2,4)
# >>>
# 6

add_txt(2,4)
# >>>
# 24

-- now this problem is solved -----

------------ this is how to work with module --------------------

				------------------------------------------


-----------------now we can see how to work with packages-------------------------

we have to create a folder in this location (new14 is the folder now I am working)
actually package is a folder

we can create a folder (package1)
 now we can create a module in this location (package1)
 	module1.py


 module1.py --->
 	
 	def func1():
 		print('this is from module1')

## now we have to learn how to call this function in app.py file 
# let see how to do it

app.py----->

import package1

# now let see if we can call this in here 

package1.func1()

# >>>
# AttributeError: module 'package1' has no attribute 'func1'


# now we can see this is have a error 
## now let see another way

package1.module1.func1()
>>>
AttributeError: module 'package1' has no attribute 'module1'

## there is a error 

so let see how to fix this problem correctly 

 app.py ------------>>

 ## this is the correct way to do this 

 from package1.module1 import func1

 func1()
>>> this is from module1

## now there is no problem
---------

# now lets try to make another module in package1 one and try to run it

package1 it already have 
module1.py 

now lets create a another module
like this 
module2.py

module2.py--------->>>

def func2():
	print('this is from module2')

now lets go to the app.py

app.py ------>>

from package1.module1 import func1
from package1.module2 import func2

func1()
func2()

# >>>
# this is from module1
# this is from module2


### there is no problem to solve



-------------- let see how to import these modules like anther modules 


ex : if we want to import numpy module, time , logging or any module 
we can import those like this

import numpy 
import time 
import logging

let see how to import own Modules like this
for that we have to create init file 

for the package1 (package1 folder)
we have to create new python file 
__init__.py

so now package1 has module1, module2 and __init__.py 

this python file is automatically run

__init__.py ---->>

print('hello')

app.py ---->>

from package1.module1 import func1
from package1.module2 import func2

func1()
func2()


>>>
hello
this is from module1
this is from module2

## so this is the out put and this is the app.py file 
## and don't need to call this init file 

## when we call the package1 it automatically call the init file 

# now let see how to do our job

__init__.py --->>

print('hello')

from .module1 import * 
from .module2 import * 

app.py  --->>

## now let remove theses from package1.module1 import * and 
# from package1.module2 import * 

app.py ---->>

import package1

package1.func1()
package1.func2()

>>>>
hello
this is from module1
this is from module2


## this is the out put 
## ------------------------------------------------
and let see can we create another function in init file

__init__.py ----->>

print('hello')

from .module1 import * 
from .module2 import * 

def func3():
	print('this is from init file')


app.py ------>>

import package1

package1.func1()
package1.func2()

package1.func3()

>>>
hello
this is from module1  
this is from module2  
this is from init file

--------------------------------------------------------------------------
		now we know how to import own Modules and packages 
		and also we know how to run those like another modules and packages


		----------------------------------------------











