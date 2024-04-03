import os
def find(path, filename):
  for entry in os.listdir(path):
    full_path = os.path.join(path, entry)
    if os.path.isfile(full_path) and entry == filename:
      # Found a matching file, print its full path
      print(full_path)
    elif os.path.isdir(full_path):
      # Recursively search within subdirectories
      find(full_path, filename)
root_path = "/home/user/data"
target_filename = "report.txt"
find(root_path, target_filename)
