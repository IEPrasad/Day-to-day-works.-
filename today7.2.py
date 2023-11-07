

		# ** ---- Abstract Classes and Methods -----

		# ** Abstract classes and methods are concepts commonly used in
		#  object-oriented programming (OOP) to define a blueprint for classes
		#  and methods that must be implemented by their subclasses. They help 
		#  ensure that certain functionality is provided by derived classes 
		#  while allowing for some level of customization and polymorphism.	

		#$$$ abstract classes can't create object 

# -------- this is not abstract class because it can make a obj 
# class phone:
# 	def func(self):
# 		pass

# obj = phone()
#>>> no error	

# ------------- we can do this like these-----


# from abc import ABC, abstractmethod

# class phone(ABC): # inherit ABC class 
# 	@abstractmethod
# 	def func(self):
# 		pass
# obj1 = phone()

# >>>^^^^^^^TypeError: Can't instantiate abstract class phone with abstract method func

# ## so this is the way how to create abstract class 

# ----------------

# from abc import ABC, abstractmethod

# class phone(ABC):
# 	@abstractmethod
# 	def func(self):
# 		pass 
# class Samsung(phone):
# 	pass 
# obj1 = Samsung()

# >>> TypeError: Can't instantiate abstract class Samsung with abstract method func



# ---------------- 

# from abc import ABC, abstractmethod

# class Phone(ABC):
# 	@abstractmethod
# 	def func(self):
# 		pass 

# class Samsung(Phone):
# 	def func(self):
# 		pass

# obj1 = Samsung()

# >>> ## we can use like this without errors















