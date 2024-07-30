import os
from PIL import Image

from imgresize import GetSize

def rename_files_in_subfolders(input_folder_path, new_width):
    for foldername, subfolders, filenames in os.walk(input_folder_path):
        for filename in filenames:
            image = Image.open(os.path.join(foldername, filename))

            # Get the current width and height
            width, height = image.size

            # Calculate the new height based on the desired width
            new_height = (height * new_width) // width

            # Resize the image
            resized_image = image.resize((new_width, new_height))

            resized_image.save(os.path.join(foldername, filename))


def main():
    new_width = GetSize()
    folder = "input"
    rename_files_in_subfolders(folder, new_width)


if __name__ == "__main__":
    main()