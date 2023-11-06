

# 			Multi Threading -2

# how to use Multi Threading with classes 
	
		To use multithreading with classes in Python, you create a class that 
		inherits from threading.Thread. Define a run() method within this class 
		to specify the code to be executed in a separate thread. Instantiate objects
		of this custom class, start the threads with start(), and, if needed, wait
		for them to finish with join(). This approach allows you to run multiple 
		threads, each executing the defined logic concurrently.

class A:
	def func(self):
		for i in range(5):
			print("Hello")

class B:
	def func(self):
		for i in range(5):
			print("Welcome")

obj1 = A()
obj2 = B()

obj1.func()
obj2.func()

>>> 
Hello
Hello
Hello
Hello
Hello
Welcome
Welcome
Welcome
Welcome
Welcome

## how to use threading with classes 

from threading import*
from time import sleep 

class A(Thread): ## inherit Thread 
	def func(self):
		for i in range(5):
			print("Hello")
			sleep(1)

class B(Thread): ## inherit Thread 
	def func(self):
		for i in range(5):
			print("Welcome")
			sleep(1)

obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()

>>> not out put 

because we must change the method name func ==>> run 
# start kiyana method eken execute karanne run kiyana method eka nisa



from threading import*
from time import sleep 

class A(Thread): ## inherit thread 
	def run(self):
		for i in range(5):
			print("Hello")
			sleep(1)

class B(Thread):
	def run(self):
		for i in range(5):
			print("Welcome")
			sleep(1)

obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()

# >>> 
# Hello
# Welcome
# Hello
# Welcome
# Hello
# Welcome
# Hello
# Welcome
# Hello
# Welcome

------------------

from threading import*
from time import sleep


class A(Thread):
	def run(self):
		for i in range (5):
			print("Hello")
			sleep(1)

class B(Thread):
	def run(self):
		for i in range (5):
			print("Welcome")
			sleep(1)

obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()
print("Bye---------")

>>>
Welcome
Bye---------
Hello
Welcome
Hello
Welcome
Hello
Welcome
Hello
Welcome


from threading import*
from time import sleep


class A(Thread):
	def run(self):
		for i in range (5):
			print("Hello",current_thread().getName())
			sleep(1)

class B(Thread):
	def run(self):
		for i in range (5):
			print("Welcome",current_thread().getName())
			sleep(1)

obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()
print("Bye---------",current_thread().getName())

# >>>
# Hello Thread-1
Welcome Thread-2
Bye--------- MainThread
Hello Thread-1
Welcome Thread-2
Hello Thread-1
Welcome Thread-2
Hello Thread-1
Welcome Thread-2
Hello Thread-1
Welcome Thread-2


------ print("Bye---------") awasanayata print kara ganimata

from threading import*
from time import sleep


class A(Thread):
	def run(self):
		for i in range (5):
			print("Hello",current_thread().getName())
			sleep(1)

class B(Thread):
	def run(self):
		for i in range (5):
			print("Welcome",current_thread().getName())
			sleep(1)

obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()

obj1.join()
obj2.join()
print("Bye---------",current_thread().getName())

## mehidi mema join bawitha kirimedi mema object dekama join unata passe print bye ---
##	kiyana eka execute wenne

>>>
Hello Thread-1
Welcome Thread-2
Hello Thread-3
Welcome Thread-4
Hello Thread-1
Welcome Thread-2
Hello Thread-3
Welcome Thread-4
Hello Thread-1
Welcome Thread-2
Hello Thread-3
Welcome Thread-4
Hello Thread-1
Welcome Thread-2
Hello Thread-3
Welcome Thread-4
Bye--------- MainThread













