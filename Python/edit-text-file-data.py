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


# 3. Remove data from the file

# To remove data, follow a similar process: 
    # Read the file contents
    # Remove the desired lines or text
    # Write the updated content back to the file

# Remove specific line (example: remove lines containing "remove this")
with open("newtextfile.txt", "r") as file:
  content = file.readlines()

# Filter out lines with "remove this"
content = [line for line in content if "remove this" not in line]

# Write the filtered content back to the file
with open("newtextfile.txt", "w") as file:
  file.writelines(content)


# summary 
# Append data: use mode "a" to add data without modifying existing data.
# Edit data: read the file, modify in memory, and overwrite the file.
# Remove data: read, filter out the unwanted content, and overwrite the file.
