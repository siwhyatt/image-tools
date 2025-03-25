# Recursively resize all images within a directory. Optionally choose which file types and whether to rename.

import os
from PIL import Image
from helpers import GetArgument

def resize_image(folder_path, new_width, file_types, create_copy):

    extensions = {
        "1": [".jpg", ".jpeg", ".png"],  # All supported types
        "2": [".jpg", ".jpeg"],          # Just JPG/JPEG
        "3": [".png"]                    # Just PNG
    }

    selected_extensions = extensions.get(file_types, extensions["1"])

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in selected_extensions):

                # Open the image file
                image_path = os.path.join(foldername, filename)
                try:
                    image = Image.open(image_path)

                    # Get the current width and height
                    width, height = image.size

                    # Calculate the new height based on the desired width
                    new_height = (height * new_width) // width

                    # Resize the image
                    resized_image = image.resize((new_width, new_height))

                    if create_copy == "1":

                        file_name, file_ext = os.path.splitext(filename)
                        # Create new filename with size info
                        new_filename = f"{file_name}_{new_width}x{new_height}{file_ext}"
                        output_path = os.path.join(foldername, new_filename)
                        resized_image.save(output_path)
                        print(f"Created copy: {output_path}")

                    else:

                        # Save the resized image with a new filename
                        resized_image.save(image_path)
                        
                        # Confirm resize
                        print(f"{image_path} resized to {str(new_width)}x{str(new_height)}")

                except Exception as e:
                    print(f"Error processing {image_path}: {e}")

def main():
    # Get the desired width of the resized images from user input
    # Get the desired width of the resized images
    new_width = int(GetArgument("Enter the desired width of the resized images: ", 1))
    
    # Get file type selection
    file_types = GetArgument(
        "Select file types to resize:\n"
        "1. All supported (jpg, jpeg, png)\n"
        "2. JPG/JPEG only\n"
        "3. PNG only\n"
        "Enter choice (1-3): ", 2)
    
    # Get resize mode (copy or overwrite)
    create_copy = GetArgument(
        "How should resized images be saved?\n"
        "1. Create a new copy (original_WIDTHxHEIGHT.ext)\n"
        "2. Replace original files\n"
        "Enter choice (1-2): ", 3)
    
    folder_path = os.getcwd()
    
    resize_image(folder_path, new_width, file_types, create_copy)

if __name__ == "__main__":
    main()
