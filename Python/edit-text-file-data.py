# 1. Add data to the file
# To add data, we can open the file in the append mode ("a")

# Append data to the file 
with open("newtextfile.txt", "a") as file:
  file.write("Appending new line to the file.\n")
  file.write("Another line of data added.\n")



# 2. Edit data in the file

# To edit specific data, we need
    # Read the contents
    # Modify the content in memory 
    # Write the modified content back to the file 

# Read, modify, and write back data (edit data)
with open("newtextfile.txt", "r")  as file:
  content = file.readlines()

# Modify specific line (example: replace "line to change" with "new content")
content = [line.replace("line to change", "new content") for line in content]

# Write the modified content back to the file
with open("newtextfile.txt", "w") as file:
  file.writeline(content)


  