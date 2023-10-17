import os
from PIL import Image

# Get the list of image files in the folder
folder_path = input("Path/to/folder ")

image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]

# Loop through each image file and resize it
for file_name in image_files:
    # Open the image file
    image = Image.open(os.path.join(folder_path, file_name))

    # Convert to black and whit
    black_and_white = image.convert("L")

	# Save the resized image with a new filename
    new_file_name = "black_and_white_" + file_name
    black_and_white.save(os.path.join(folder_path, new_file_name))

    print(f"All image files in {folder_path} converted to black and white")