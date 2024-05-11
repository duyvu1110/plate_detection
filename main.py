import os

# Folder path
folder_path = "test_data"

# Initialize a counter for the number of files
file_count = 0

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    # Check if it's a file (not a directory)
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_count += 1

print(f"Number of files in {folder_path}: {file_count}")
