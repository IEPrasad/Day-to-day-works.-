

				|File Handling|| OS Module|
	
	** File handling in Python is a crucial aspect of working with files and 
	directories on your system. The os module is a standard library module in 
	Python that provides various functions to interact with the operating system, 
	including file and directory operations. Here's an overview of how to use the os
	module for file handling:


import os

		1: Working with Directions 

	** Get the current working directory:
		current_directory = os.getcwd()

	** Change the current working directory:
		os.chdir("new_directory_path")

	** List files and directories in a directory:
		file_list = os.listdir("directory_path")

	** Create a new directory:
		os.mkdir("new_directory_name")

	** Create a new directory and its parent directories if they don't exist:
		os.makedirs("path/to/new_directory")

	** Remove an empty directory:
		os.rmdir("directory_name")

	** Remove a directory and its contents (use with caution):
		os.removedirs("path/to/directory")

			-------------

		2. File Operations:

	** Check if a file or directory exists:
		if os.path.exists("file_or_directory_path"):
    	# File or directory exists

    ** Check if it's a file:
    	if os.path.isfile("file_path"):
	    # It's a file

	** Check if it's a directory:
		if os.path.isdir("directory_path"):
	    # It's a directory

	** Rename a file or directory:
		os.rename("old_name", "new_name")

	** Delete a file (use with caution):
		os.remove("file_name")

			--------------------


		3. Path Manipulation:

	** Join paths to create a valid path for the current OS:
		full_path = os.path.join("directory", "subdirectory", "file.txt")

	** Split a path into its components (directory, filename):
		directory, filename = os.path.split("path/to/file.txt")


---------- The 'os' module provides a comprehensive set of functions for file 
	and directory operations, making it a poweful tool for working with the
	file system in a platform-independent way. However, it's essential to be
	cautions when using functions that delete or modify files and directories,
	as they can result in data los if not used carefully.

					-----------------------------------












