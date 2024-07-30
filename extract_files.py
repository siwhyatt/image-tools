import os

def extract_files_from_subfolders(input_folder_path, output_folder_path):
    for foldername, subfolders, filenames in os.walk(input_folder_path):
        for filename in filenames:
            old_path = os.path.join(foldername, filename)
            new_path = os.path.join(output_folder_path, filename)
            os.rename(old_path, new_path)
            print(f"Moved: {old_path} to {new_path}")

# Replace 'path_to_your_directory' with the actual path to your parent directory
input_folder_path = 'input'
ouput_folder_path = "output"
extract_files_from_subfolders(input_folder_path, ouput_folder_path)