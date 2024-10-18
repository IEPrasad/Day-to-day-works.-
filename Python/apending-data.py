import datetime

def append_data(file_name, data):
  with open(file_name, "a") as file:
    timestamp = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] {data}\n")
  print(f"Appended data to {file_name}")


# Usage
append_data("newtextfile.txt", "This is an advanced log entry.")