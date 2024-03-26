# Recursively rename files in a directory from csv

import os
import csv

# Define the path to the directory and the CSV file
folder_path = 'input'
csv_file_path = 'filerename.csv'

# Function to read the CSV and return a dictionary of old-new name pairs
def read_csv(file_path):
    name_mapping = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            old_name, new_name = row
            name_mapping[old_name] = new_name
    return name_mapping

# Rename files based on the CSV mapping
def rename_files(folder_path, name_mapping):
    for file_name in os.listdir(folder_path):
        # Check if the file name is in the dictionary
        if file_name in name_mapping:
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, name_mapping[file_name])
            # Check if a file with the new name already exists
            if not os.path.exists(new_file_path):
                os.rename(old_file_path, new_file_path)
                print(f'Renamed "{file_name}" to "{name_mapping[file_name]}"')
            else:
                print(f'Cannot rename "{file_name}" to "{name_mapping[file_name]}" because the target file already exists.')

# Read the CSV file to get the mapping
name_mapping = read_csv(csv_file_path)

# Rename the files in the folder based on the CSV
rename_files(folder_path, name_mapping)
