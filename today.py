
#				 Multi Threading - 1 

** 			what is multi tasking 
	 
   refers to the ability of a computer or an operating system to execute multiple
	 tasks or processes simultaneously. It allows a computer to switch rapidly 
	 between different tasks, giving the appearance of parallel execution. 
	 Multitasking enables users to run multiple applications or perform multiple 
	 actions on a computer, like browsing the web, listening to music, and editing 
	 documents, without having to wait for one task to complete before starting 
	 another. This is achieved through efficient scheduling and resource management
	 by the operating system, allowing for better utilization of the computer's 
	 processing power and resources.


** 		What is " multi threading "
	
	refers to the ability of a computer or an operating system to execute multiple 
	tasks or processes simultaneously. It allows a computer to switch rapidly
	between different tasks, giving the appearance of parallel execution.
	Multitasking enables users to run multiple applications or perform multiple 
	actions on a computer, like browsing the web, listening to music, and editing 
	documents, without having to wait for one task to complete before starting 
	another. This is achieved through efficient scheduling and resource management 
	by the operating system, allowing for better utilization of the computer's 
	processing power and resources.


--------------------------

def func1():
	for i in range (5):
		print("Good")

def func2():
	for i in range (5):
		print("Bye")

func1()
func2()

# >>> The out put 
# Good
# Good
# Good
# Good
# Good
# Bye
# Bye
# Bye
# Bye
# Bye


# $$ we have to call these both of function in one time usin threading 

import threading 
from time import sleep

def func1():
	for i in range (5):
		print("Good")
		## making delay
		sleep(1) 

def func2():
	for i in range (5):
		print("Bye")
		## making delay
		sleep(1)

## making therads 
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

## execute 

t1.start()
## making delay
sleep(0.2)
t2.start()

# >>>
# Good
# Bye
# Good
# Bye
# Good
# Bye
# Good
# Bye
# Good
# Bye



