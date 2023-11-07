

	# ------------**	Multi Threading -3|Synchronization| --------------

	# **-- Synchronization, in the context of multithreading and concurrent programming, 
	# is a mechanism used to coordinate and control the execution of multiple threads 
	# to ensure that they work together in an orderly and predictable manner. It is 
	# essential for preventing race conditions, data corruption, and ensuring thread safety.
	# Synchronization techniques help manage shared resources and critical sections of code 
	# where multiple threads may access or modify data simultaneously.



# import time 

# def dispaly():
# 	for i in range (3):
# 		print("hello")
# 		time.sleep(1)

# dispaly()
# >>> 
# hello
# hello
# hello

# ---------

# import time
# from threading import*

# def dispaly():
# 	for i in range (3)
# 		print(threading.currentThread().name)
# 		time.sleep(1)


# t1 = Thread(target=dispaly)
# t1.start()

# >>>
# hello
# hello
# hello

 
# --------------------

# import time
# from threading import*
# import threading

# def dispaly():
# 	for i in range (3):
# 		print(threading.currentThread().name)
# 		time.sleep(1)


# t1 = Thread(target=dispaly)
# t1.start()

# >>>
# Thread-1 (dispaly)
# Thread-1 (dispaly)
# Thread-1 (dispaly)


# ----------------------

# import time
# from threading import*
# import threading

# def dispaly():
# 	for i in range (3):
# 		print(threading.currentThread().name)
# 		time.sleep(1)


# t1 = Thread(target=dispaly)
# t2 = Thread(target=dispaly) ## create another thread 
# t1.start()
# t2.start()



# >>>
# Thread-1 (dispaly)
# Thread-2 (dispaly)
# Thread-2 (dispaly)
# Thread-1 (dispaly)
# Thread-1 (dispaly)
# Thread-2 (dispaly)

		## this is the problem 
		## it can solve by using lock class with aquire() and release()

# ---------------



import time
from threading import*
import threading

lock = Lock()

def dispaly():
	lock.acquire()
	for i in range (3):
		print(threading.currentThread().name)
		time.sleep(1)
	lock.release()

t1 = Thread(target=dispaly)
t2 = Thread(target=dispaly) ## create another thread 
t1.start()
t2.start()

# >>>
# Thread-1 (dispaly)
# Thread-1 (dispaly)
# Thread-1 (dispaly)
# Thread-2 (dispaly)
# Thread-2 (dispaly)
# Thread-2 (dispaly)




















