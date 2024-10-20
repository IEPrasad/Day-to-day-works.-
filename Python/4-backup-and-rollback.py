# 4. Advanced Code: Transactional File Editing (Backup and Rollback)

# Adding backup and rollback capabilities in case the file operation fails:
import shutil

def transactional_edit(file_name, old_text, new_text):
    backup_file_name = file_name + ".bak"
    try:
        # Create a backup
        shutil.copy(file_name, backup_file_name)
        print(f"Backup created: {backup_file_name}")

        # Perform edit (same regex approach)
        with open(file_name, "r") as file:
            content = file.read()

        content = re.sub(old_text, new_text, content)

        with open(file_name, "w") as file:
            file.write(content)

        print(f"Edit successful: {file_name}")
    except Exception as e:
        print(f"Error occurred: {e}")
        # Rollback to the original state in case of error
        shutil.copy(backup_file_name, file_name)
        print(f"Rolled back to backup: {backup_file_name}")
    finally:
        # Optionally, delete the backup
        if os.path.exists(backup_file_name):
            os.remove(backup_file_name)

# Usage
transactional_edit("newtextfile.txt", r"\bSOMETHING\b", "NEW_VALUE")
