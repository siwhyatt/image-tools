import os
import shutil

def move_files_to_single_directory(root_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            source_path = os.path.join(foldername, filename)
            destination_path = os.path.join(destination_dir, filename)

            # Check if the file already exists in the destination directory
            if os.path.exists(destination_path):
                # You can handle naming conflicts here. For now, let's just add a suffix.
                base, ext = os.path.splitext(filename)
                filename = f"{base}_duplicate{ext}"
                destination_path = os.path.join(destination_dir, filename)

            shutil.move(source_path, destination_path)
            print(f"Moved: {source_path} to {destination_path}")

# Replace 'path_to_your_directory' with the actual path to your parent directory
parent_directory = 'input'

# Replace 'path_to_destination_directory' with the desired path for the new directory
destination_directory = 'output'

move_files_to_single_directory(parent_directory, destination_directory)
