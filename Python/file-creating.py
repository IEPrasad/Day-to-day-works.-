# Create and write to the .txt file 
with open("newtextfile.txt", "w") as file:
  file.write("This is sample text.\n")
  file.write("We can add multiple lines of data here.\n")

# Open the file to read and display the contents 
with open("newtextfile.txt", "r") as file:
  content = file.read()
  print("File content:\n", content)


# Check the details such as name, mode, and whether it is closed

print("\nFile details:")
print("File name:", file.name)
print("File mmode", file.mode)
print("Is File closed:", file.closed)


# Display file size
import os
file_size = os.path.getsize("newtextfile.txt")
print("File size:", file_size, "bytes")

