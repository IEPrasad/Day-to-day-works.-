
	# |Python Tutorial -51| | OS module in python |


import os 

# 1) Get the current working directory:

# print(os.getcwd())
# >>>
# C:\Users\isuru\OneDrive\Desktop\commit
# ** This code uses the os module to print the current working directory
--------------------

# 2) Change the current working directory:
 
 ### first we have to create a folder in a desktop 
 ## now we can copy the location of these new folder 
 ## then we can understand how to do this 
 		## and this is the location of these new folder
 			# C:\Users\isuru\OneDrive\Desktop\python11

# now we can change our working directory

# print("this is our first location")
# print(os.getcwd()) 
# print()
# os.chdir(r'C:\Users\isuru\OneDrive\Desktop\python11')
## we must put the 'r' like these or we must change \ as a /

# print("this is our new location")
# print(os.getcwd()) 

# >>>
# this is our first location
# C:\Users\isuru\OneDrive\Desktop\commit

# this is our new location
# C:\Users\isuru\OneDrive\Desktop\python11

##$ now we have to prove this 
# by using 	"os.listdir"

# print(os.listdir())

# >>>
# this is our first location
# C:\Users\isuru\OneDrive\Desktop\commit

# this is our new location
# C:\Users\isuru\OneDrive\Desktop\python11
# []

## so we already know nothing is have new folder and many of things have
	# commit folder


# these os.listdir() method showing us what are in our folder

---------------------------

# 3) create a directory

# os.chdir(r'C:\Users\isuru\OneDrive\Desktop\python11')
# os.mkdir('hello')
# print(os.listdir())
# >>>
# ['hello']

----------------------------

# 4) remove a directory

# os.chdir(r'C:\Users\isuru\OneDrive\Desktop\python11')
# os.rmdir('Python')


-------------------------------------

# 5) rename a directory name 

# os.rename('hello','welcome')

--------------------------------------

# 6) how to see about os module

# print(dir(os))

# >>>

# ['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND',
# 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR',
#  'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY',
#  'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK',
#  'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory',
#   '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath',
#    '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory',
#    'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath',
#    'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle',
#     'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 
#     'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 
#     'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 
#     'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 
#     'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 
#     'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 
#     'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 
#     'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 
#     'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 
#     'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 
#     'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 
#     'waitstatus_to_exitcode', 'walk', 'write']


# print(len(dir(os)))
# # >>> 
# 156

# there is 156 methods has the os module

-------------------------------


print(help(os.mkdir))

>>>

Help on built-in function mkdir in module nt:

mkdir(path, mode=511, *, dir_fd=None)
    Create a directory.

    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

    The mode argument is ignored on Windows. Where it is used, the current umask
    value is first masked out.

None


------------------------------------------

SUMMARY 

		1- os.getcwd()
		2- os.chdir()
		3- os.mkdir()
		4- os.rmdir()
		5- os.rename()
		6- print(dir(os))
		7- print(len(dir(os)))
		8- print(help(os.mkdir))



------------------------- 










