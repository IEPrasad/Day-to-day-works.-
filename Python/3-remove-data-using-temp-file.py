# 3. Advanced Code: Remove Data In-Place Using Temp File

# Efficient in-place file editing using a temporary file to avoid overwriting the original during read/write operations:

import os

def remove_lines(file_name, text_to_remove):
    temp_file_name = file_name + ".tmp"

    with open(file_name, "r") as file, open(temp_file_name, "w") as temp_file:
        for line in file:
            if text_to_remove not in line:  # Exclude lines with unwanted text
                temp_file.write(line)

    os.remove(file_name)  # Remove original file
    os.rename(temp_file_name, file_name)  # Rename temp file to original
    print(f"Removed lines containing '{text_to_remove}' from {file_name}")

# Usage
remove_lines("newtextfile.txt", "remove this")


# Temp File Approach: Using a temporary file ensures safe file operations. If something goes wrong, the original file is intact.

# Line-by-line Filtering: Removes lines that match the specific string.