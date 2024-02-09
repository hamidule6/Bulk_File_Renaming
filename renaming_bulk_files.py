import os

# directory location containing files
directory = "/path/to/your/file/"

# Specify the part you want to remove from the file names
part_to_remove = "part_to_remove"

# List all files in the directory
files = os.listdir(directory)

# Iterate through each file and rename it
for file_name in files:
    # Check if the part to remove exists in the file name
    if part_to_remove in file_name:
        # Construct the new file name by removing the part to remove
        new_name = file_name.replace(part_to_remove, "")
        # Rename the file
        os.rename(os.path.join(directory, file_name), os.path.join(directory, new_name))

print("Renaming complete.")
