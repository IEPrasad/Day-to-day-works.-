# Editing data using regular expressions to find and replace patterns in a file:


import re

def edit_data(file_name, old_text, new_text):
    with open(file_name, "r") as file:
        content = file.read()

    # Use regular expressions to find and replace the old text
    content = re.sub(old_text, new_text, content)

    with open(file_name, "w") as file:
        file.write(content)
    print(f"Edited content in {file_name}")

# Usage
edit_data("newtextfile.txt", r"\bOLD_VALUE\b", "NEW_VALUE")


'''
Regex Search: Using re.sub(), you can replace patterns instead of simple text.
Flexible matching: This allows for more complex searches, like case-insensitive, word boundaries (\b), or even replacing patterns based on conditions.

'''