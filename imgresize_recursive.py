import os
from PIL import Image

def resize_image(input_path, output_path, new_width):
    for foldername, subfolders, filenames in os.walk(input_path):
        for filename in filenames:
            if filename.endswith(".jpg"):
                # Construct the relative path for the output folder
                relative_path = os.path.relpath(foldername, input_path)
                output_folder = os.path.join(output_path, relative_path)

                # Create the output folder if it doesn't exist
                os.makedirs(output_folder, exist_ok=True)

                # Open the image file
                image_path = os.path.join(foldername, filename)
                image = Image.open(image_path)

                # Get the current width and height
                width, height = image.size

                # Calculate the new height based on the desired width
                new_height = (height * new_width) // width

                # Height as string
                height_string = str(new_height)

                # Resize the image
                resized_image = image.resize((new_width, new_height))

                # Save the resized image with a new filename
                new_file_name = "resized_" + str(new_width) + "_x_" + height_string + "_px_" + filename
                output_file_path = os.path.join(output_folder, new_file_name)
                resized_image.save(output_file_path)

# Get the desired width of the resized images from user input
while True:
    try:
        new_width = int(input("Enter the desired width of the resized images: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value.")

input_folder_path = "input/"
output_folder_path = "output/"

resize_image(input_folder_path, output_folder_path, new_width)
