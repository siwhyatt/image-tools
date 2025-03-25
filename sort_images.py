# NOTE Sort images by file extention

import os
import shutil

def rename_jpeg_to_jpg():
    """
    Renames all files with the .jpeg extension to .jpg in the given directory.
    """
    directory = os.getcwd()

    try:
        for filename in os.listdir(directory):
            if filename.lower().endswith(".jpeg"):
                old_filepath = os.path.join(directory, filename)
                new_filename = filename[:-5] + ".jpg"  # Remove ".jpeg" and add ".jpg"
                new_filepath = os.path.join(directory, new_filename)

                os.rename(old_filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")

        print("Renaming complete.")

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def move_image_files_based_on_ext():
    # Get CWD
    cwd = os.getcwd()

    # Create folders for each file type
    filetypes =['jpg', 'png']

    for filetype in filetypes:
        if not os.path.exists(filetype):
            os.makedirs(filetype)

    # Get all files in the CWD (not subdirectories)
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

    # Walk through CWD
    for file in files:
        for filetype in filetypes:
            if file.lower().endswith(filetype):
                source_path = os.path.join(cwd, file)
                destination_path = os.path.join(cwd, filetype, file)

                try:
                    shutil.move(source_path, destination_path)
                    print(f"Moved: {source_path} to {destination_path}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")


def main():
    rename_jpeg_to_jpg()
    move_image_files_based_on_ext()


if __name__ == '__main__':
    main()

